"""
linkeddatatools - a Python library for RDF graph structuring and exchange.
"""
#IMPORT PACKAGES
from lib2to3.pytree import Node
import numpy as np 
import cv2 
import open3d as o3d 
import json  
import os 
import re
import uuid    
import ntpath

import matplotlib.pyplot as plt #conda install -c conda-forge matplotlib
#import torch #conda install -c pytorch pytorch
import pye57 #conda install xerces-c  =>  pip install pye57
import xml.etree.ElementTree as ET 
# from pathlib import Path
import math
from datetime import datetime

# import ifcopenshell.util
# import ifcopenshell.geom as geom
# from ifcopenshell.util.selector import Selector
# from ifcopenshell.ifcopenshell_wrapper import file

# import APIs
import rdflib
from rdflib import Graph, plugin
from rdflib.serializer import Serializer #pip install rdflib-jsonld https://pypi.org/project/rdflib-jsonld/
from rdflib import Graph
from rdflib import URIRef, BNode, Literal
from rdflib.namespace import CSVW, DC, DCAT, DCTERMS, DOAP, FOAF, ODRL2, ORG, OWL, \
                           PROF, PROV, RDF, RDFS, SDO, SH, SKOS, SOSA, SSN, TIME, \
                           VOID, XMLNS, XSD


#IMPORT MODULES watch out for circular imports
import geomapi
import geomapi.pointcloudnode
import geomapi.meshnode
import geomapi.imagenode
import geomapi.bimnode

# import geomapi.node
# import geomapi.geometrynode
# import geomapi.meshnode
# import geomapi.pointcloudnode

# from geomapi.node import Node
# from geomapi.geometrynode import GeometryNode
# from geomapi.bimnode import BIMnode
# from geomapi.meshnode import MeshNode
# from geomapi.pointcloudnode import PointCloudNode
# from geomapi.imagenode import ImageNode

def e57xml_to_nodes(xmlPath :str):
    """Parse xml file that is created with E57lib e57xmldump.exe

    Args:
        path (string):  e57 xml file path e.g. "D:\\Data\\2018-06 Werfopvolging Academiestraat Gent\\week 22\\PCD\\week 22 lidar_CC.xml"
            
    Returns:
        A list of pointcloudnodes with the xml metadata 
    """
    try:
        #E57 XML file structure
        #e57Root
        #   >data3D
        #       >vectorChild
        #           >pose
        #               >rotation
        #               >translation
        #           >cartesianBounds
        #           >guid
        #           >name
        #           >points recordCount
        #   >images2D
        mytree = ET.parse(xmlPath)
        root = mytree.getroot()  
        nodelist=[]   
        e57Path=xmlPath.replace('.xml','.e57')       

        for idx,e57node in enumerate(root.iter('{http://www.astm.org/COMMIT/E57/2010-e57-v1.0}vectorChild')):
            node=geomapi.pointcloudnode.PointCloudNode() 
            node.name=get_filename(e57Path) +'_'+str(idx)
            node.guid='{'+str(uuid.uuid1())+'}' 
            node.e57Path=e57Path
            node.timestamp=get_timestamp(e57Path)
            node.set_from_e57_xml_node(e57node) # DIT MOET NOG IN ORDE WORDEN GEBRACHT
            node.e57XmlPath=xmlPath
            node.e57Index=idx
            nodelist.append(node)
        return nodelist
    except:
        print('xmlPath not recognized. Please run .\e57xmldump on target e57 files and store output xml files somewhere in session folder. If formatting error occurs, manually remove <?xml version="1.0" encoding="UTF-8"?> from xml file.')

def e57header_to_nodes(e57Path:str):
    """
    Parse e57 file header that is created with E57lib e57xmldump.exe

    Args:
        path (string):  e57 xml file path e.g. "D:\\Data\\2018-06 Werfopvolging Academiestraat Gent\\week 22\\PCD\\week 22 lidar_CC.xml"
            
    Returns:
        A list of pointcloudnodes with the xml metadata 
    """
    try:
        nodelist=[]   
        e57 = pye57.E57(e57Path)   
        for idx in range(e57.scan_count):
            header = e57.get_header(idx)
            node=geomapi.pointcloudnode.PointCloudNode()
            node.name=get_filename(e57Path) +'_'+str(idx)
            node.timestamp=get_timestamp(e57Path)
            node.guid='{'+str(uuid.uuid1())+'}' 
            node.set_from_e57_header(header) 
            node.e57Index=idx
            node.e57Path=e57Path
            nodelist.append(node)
        return nodelist
    except:
        print('e57header error')

def pcd_to_node(path:str)-> geomapi.pointcloudnode.PointCloudNode:
    """
    Parse pcd file to PointCloudNode

    Args:
        path (string):  e57 xml file path e.g. "D:\\Data\\2018-06 Werfopvolging Academiestraat Gent\\week 22\\PCD\\week 22 lidar_CC.xml"
            
    Returns:
        A pointcloudnodes with metadata 
    """   
    try:
        node=geomapi.pointcloudnode.PointCloudNode() 
        node.name=get_filename(path)
        node.timestamp=get_timestamp(path)
        node.guid='{'+str(uuid.uuid1())+'}' 
        node.path=path
        node.get_data()
        node.set_from_pcd()
        return node
    except:
        print('pcd import error')
        return None

def e57_to_pcd(e57scan) ->o3d.geometry.PointCloud:
    """
    Convert pye57.E57scan to o3d.geometry.PointCloud
    Args:
        e57scan    
    Returns:
        o3d.geometry.PointCloud
    """
    try:
        x_ndarray=e57scan.get('cartesianX')
        y_ndarray=e57scan.get('cartesianY')
        z_ndarray=e57scan.get('cartesianZ')

        array= np.vstack(( x_ndarray,y_ndarray,z_ndarray)).T
        points = o3d.utility.Vector3dVector(array)
        return o3d.geometry.PointCloud(points)
    except:
        print("Conversion from e57 to o3d.geometry.PointCloud failed!")
        return None    

def get_if_exist(data, key):
    if key in data:
        return data[key]
    return None

def string_to_rotation_matrix(matrixString :str) -> np.array:
    list=matrixString.split(' ')
    rotationMatrix=np.array([[float(list[0]),float(list[1]),float(list[2]),0],
                             [float(list[3]),float(list[4]),float(list[5]),0],
                             [float(list[6]),float(list[7]),float(list[8]),0],
                             [0,0,0,1]])
    return rotationMatrix

def string_to_array(string : str)-> np.array:
    list=string.split(' ')
    floatlist=[]
    for x in list:
        floatlist.append(float(x))
    return np.array(floatlist)

def graph_to_nodes(graph : Graph):
    nodelist=[]
    for subject in graph.subjects(RDF.type):
        # print(str(session_graph.value(subject=s,predicate=e57.recordCount) ))  
        node=subject_to_node(graph,subject)
        nodelist.append(node)
    return nodelist

def subject_to_node(graph : Graph , subject : URIRef):
    # nodeType=str(graph.subjects(subject))
    nodeType=literal_to_string(graph.value(subject=subject,predicate=RDF.type))

    exif = rdflib.Namespace('http://www.w3.org/2003/12/exif/ns')
    graph.bind('exif', exif)
    geo=rdflib.Namespace('http://www.opengis.net/ont/geosparql#') #coordinate system information
    graph.bind('geo', geo)
    gom=rdflib.Namespace('https://w3id.org/gom#') # geometry representations => this is from mathias
    graph.bind('gom', gom)
    omg=rdflib.Namespace('https://w3id.org/omg#') # geometry relations
    graph.bind('omg', omg)
    fog=rdflib.Namespace('https://w3id.org/fog#')
    graph.bind('fog', fog)
    v4d=rdflib.Namespace('https://w3id.org/v4d/core#')
    graph.bind('v4d3D', v4d)
    v4d3D=rdflib.Namespace('https://w3id.org/v4d/3D#')
    graph.bind('v4d3D', v4d3D)
    openlabel=rdflib.Namespace('https://www.asam.net/index.php?eID=dumpFile&t=f&f=3876&token=413e8c85031ae64cc35cf42d0768627514868b2f')
    graph.bind('openlabel', openlabel)
    e57=rdflib.Namespace('http://libe57.org/')
    graph.bind('e57', e57)
    xcr=rdflib.Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
    graph.bind('xcr', xcr)
    ifc=rdflib.Namespace('http://ifcowl.openbimstandards.org/IFC2X3_Final#')
    graph.bind('ifc', ifc)

    if 'BIMnode' in nodeType:
        node=geomapi.bimnode.BIMNode()
        node.vertexCount = literal_to_int(graph.value(subject=subject,predicate=e57.recordCount)) 
        node.faceCount = literal_to_int(graph.value(subject=subject,predicate=v4d.faceCount)) 
        node.ifc = literal_to_string(graph.value(subject=subject,predicate=ifc.file))   
        node.ifcElement = literal_to_string(graph.value(subject=subject,predicate=ifc.element))  
        node.cartesianBounds=literal_to_cartesianBounds(graph.value(subject=subject,predicate=e57.cartesianBounds)) 

    elif 'MeshNode' in nodeType:
        node=geomapi.meshnode.MeshNode()
        node.vertexCount = literal_to_int(graph.value(subject=subject,predicate=e57.recordCount)) 
        node.faceCount = literal_to_int(graph.value(subject=subject,predicate=v4d.faceCount)) 
        node.cartesianBounds=literal_to_cartesianBounds(graph.value(subject=subject,predicate=e57.cartesianBounds)) 

    elif 'PointCloudNode' in nodeType:
        node=geomapi.pointcloudnode.PointCloudNode()
        node.pointCount = literal_to_int(graph.value(subject=subject,predicate=e57.recordCount)) 
        node.labels = literal_to_int(graph.value(subject=subject,predicate=v4d.labels)) 
        node.labelInfo = literal_to_string(graph.value(subject=subject,predicate=v4d.labelInfo))  
        node.classification = literal_to_string(graph.value(subject=subject,predicate=v4d.classification))  
        node.e57index = literal_to_int(graph.value(subject=subject,predicate=e57.e57index)) 
        node.cartesianBounds=literal_to_cartesianBounds(graph.value(subject=subject,predicate=e57.cartesianBounds)) 

    elif 'ImageNode' in nodeType:
        node=geomapi.imagenode.ImageNode()  
        node.xResolution = literal_to_float(graph.value(subject=subject,predicate=exif.xResolution)) 
        node.yResolution = literal_to_float(graph.value(subject=subject,predicate=exif.yResolution)) 
        node.resolutionUnit = literal_to_string(graph.value(subject=subject,predicate=exif.resolutionUnit)) 
        node.imageWidth = literal_to_float(graph.value(subject=subject,predicate=exif.imageWidth)) 
        node.imageHeight = literal_to_float(graph.value(subject=subject,predicate=exif.imageLength)) 
        node.focalLength = literal_to_float(graph.value(subject=subject,predicate=xcr.FocalLength35mm))  
        node.principalPointU= literal_to_float(graph.value(subject=subject,predicate=xcr.PrincipalPointU))  
        node.principalPointV= literal_to_float(graph.value(subject=subject,predicate=xcr.PrincipalPointV))  
    
    elif 'SessionNode' in nodeType:
        node=geomapi.sessionnode.SessionNode()  
        node.projectNumber = literal_to_string(graph.value(subject=subject,predicate=v4d.projectNumber))
        node.projectType = literal_to_string(graph.value(subject=subject,predicate=v4d.project_type))
    else:
        node=geomapi.node.Node()

    #convert literals to node
    node.name = str(subject).replace('http://','') 
    node.guid = literal_to_string(graph.value(subject=subject,predicate=RDFS.label))  
    node.sessionName = literal_to_string(graph.value(subject=subject,predicate=v4d.path))   
    node.timestamp = literal_to_string(graph.value(subject=subject,predicate=openlabel.timestamp))  
    node.sensor = literal_to_string(graph.value(subject=subject,predicate=openlabel.sensor))  
    node.cartesianTransform=literal_to_cartesianTransform(graph.value(subject=subject,predicate=openlabel.cartesianTransform))
    node.geospatialTransform=literal_to_geospatialTransform(graph.value(subject=subject,predicate=openlabel.geospatialTransform))
    node.coordinateSystem = literal_to_string(graph.value(subject=subject,predicate=gom.hasCoordinateSystem))   
    node.accuracy = literal_to_float(graph.value(subject=subject,predicate=v4d.accuracy)) 
    node.path = literal_to_string(graph.value(subject=subject,predicate=v4d.path))  
    return node

def get_paths_in_class(cls) -> list: 
    """
    returns list of paths in the class
    """  
    return [i for i in cls.__dict__.keys() if 'path' in i[:1]] 

def match_uri(attribute :str):
    """
    Match attribute name with Linked Data URI's. Non-matches are serialized as V4D."attribute"
    """
    #NODE
    
    exif = rdflib.Namespace('http://www.w3.org/2003/12/exif/ns')
    geo=rdflib.Namespace('http://www.opengis.net/ont/geosparql#') #coordinate system information
    gom=rdflib.Namespace('https://w3id.org/gom#') # geometry representations => this is from mathias
    omg=rdflib.Namespace('https://w3id.org/omg#') # geometry relations
    fog=rdflib.Namespace('https://w3id.org/fog#')
    v4d=rdflib.Namespace('https://w3id.org/v4d/core#')
    v4d3D=rdflib.Namespace('https://w3id.org/v4d/3D#')
    openlabel=rdflib.Namespace('https://www.asam.net/index.php?eID=dumpFile&t=f&f=3876&token=413e8c85031ae64cc35cf42d0768627514868b2f')
    e57=rdflib.Namespace('http://libe57.org/')
    xcr=rdflib.Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
    ifc=rdflib.Namespace('http://ifcowl.openbimstandards.org/IFC2X3_Final#')

    if attribute == 'guid':
        return RDFS.label
    elif attribute == 'sessionName':
        return RDFS.label
    elif attribute == 'timestamp':
        return openlabel.timestamp
    elif attribute == 'sensor':
        return openlabel.sensor
    elif attribute == 'cartesianBounds':
        return  e57.cartesianBounds
    elif attribute == 'accuracy':
        return v4d.accuracy
    elif attribute == 'cartesianTransform':
        return openlabel.cartesianTransform
    elif attribute == 'geospatialTransform':
        return openlabel.geospatialTransform
    elif attribute == 'coordinateSystem':
        return gom.hasCoordinateSystem
    elif attribute == 'path':
        return v4d.path
    elif attribute == 'sessionPath':
        return v4d.sessionPath
    #GEOMETRYNODE
    elif attribute == 'features3d':
        return v4d.features3d
    #BIMNODE
    elif attribute == 'vertexCount':
        return e57.recordCount
    elif attribute == 'faceCount':
        return v4d.faceCount
    elif attribute == 'ifc':
        return ifc.file
    elif attribute == 'ifcElement':
        return ifc.element
    #PCDNODE
    elif attribute == 'pointCount':
        return e57.recordCount
    elif attribute == 'labels':
        return v4d.labels
    elif attribute == 'labelInfo':
        return v4d.labelInfo
    elif attribute == 'classification':
        return v4d.classification
    elif attribute == 'e57XmlPath':
        return e57.e57XmlPath
    elif attribute == 'e57Path':
        return e57.e57Path
    elif attribute == 'e57Index':
        return e57.e57Index
    elif attribute == 'e57Image':
        return e57.e57Image
    #IMGNODE
    elif attribute == 'xResolution':
        return exif.xResolution
    elif attribute == 'yResolution':
        return exif.yResolution
    elif attribute == 'resolutionUnit':
        return exif.resolutionUnit
    elif attribute == 'imageWidth':
        return exif.imageWidth
    elif attribute == 'imageHeight':
        return exif.imageLength
    elif attribute == 'focalLength':
        return xcr.FocalLength35mm
    elif attribute == 'principalPointU':
        return xcr.PrincipalPointU
    elif attribute == 'principalPointV':
        return xcr.PrincipalPointV
    elif attribute == 'distortionCoeficients':
        return xcr.distortionCoeficients
    else:
        return URIRef('v4d.'+str(attribute))

def bind_ontologies(graph : Graph)->Graph:    
    """
    Bind additional ontologies that aren't in rdflib
    """
    exif = rdflib.Namespace('http://www.w3.org/2003/12/exif/ns')
    graph.bind('exif', exif)
    geo=rdflib.Namespace('http://www.opengis.net/ont/geosparql#') #coordinate system information
    graph.bind('geo', geo)
    gom=rdflib.Namespace('https://w3id.org/gom#') # geometry representations => this is from mathias
    graph.bind('gom', gom)
    omg=rdflib.Namespace('https://w3id.org/omg#') # geometry relations
    graph.bind('omg', omg)
    fog=rdflib.Namespace('https://w3id.org/fog#')
    graph.bind('fog', fog)
    v4d=rdflib.Namespace('https://w3id.org/v4d/core#')
    graph.bind('v4d3D', v4d)
    v4d3D=rdflib.Namespace('https://w3id.org/v4d/3D#')
    graph.bind('v4d3D', v4d3D)
    openlabel=rdflib.Namespace('https://www.asam.net/index.php?eID=dumpFile&t=f&f=3876&token=413e8c85031ae64cc35cf42d0768627514868b2f')
    graph.bind('openlabel', openlabel)
    e57=rdflib.Namespace('http://libe57.org/')
    graph.bind('e57', e57)
    xcr=rdflib.Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
    graph.bind('xcr', xcr)
    ifc=rdflib.Namespace('http://ifcowl.openbimstandards.org/IFC2X3_Final#')
    graph.bind('ifc', ifc)
    return graph

def literal_to_cartesianTransform(literal:Literal) -> np.array:
    cartesianTransform=str(literal)
    if 'None' not in cartesianTransform:
        transform=np.empty([0,0], dtype=float)
        stringList = re.findall(r"\[(.+?)\]", cartesianTransform)
        for list in stringList:
            temp=list.strip('[]')
            res=np.fromstring(temp, dtype=float, sep=' ')
            transform=np.append(transform,res)
        transform = transform.reshape((4,4))
        return transform
        # temp=temp.strip('[]')
        # res = list(map(float, temp.split(', '))) 
        # return [[res[0],res[1],res[2],res[3]],
        #         [res[4],res[5],res[6],res[7]],
        #         [res[8],res[9],res[10],res[11]],
        #         [res[12],res[13],res[14],res[15]]]
    else:
        return None  

def rotation_and_translation_to_transformation_matrix(rotation: np.array, translation: np.array)->np.array:
    if rotation.size ==9 and len(translation) ==3:    
        return np.array([[ rotation[0,0],rotation[0,1],rotation[0,2], translation[0]],
                        [ rotation[1,0],rotation[1,1],rotation[1,2], translation[1]],
                        [ rotation[2,0],rotation[2,1],rotation[2,2], translation[2]],
                        [ 0,0,0,1]])
    else:
        return None

def cartesian_bounds_to_cartesian_transform(cartesianBounds:np.array) ->np.array:
    if len(cartesianBounds) !=6:
        return None
    else:
        matrix=np.zeros([4,4])
        np.fill_diagonal(matrix,1)
        matrix[3]=(cartesianBounds[1]-cartesianBounds[0])/2
        matrix[7]=(cartesianBounds[3]-cartesianBounds[2])/2
        matrix[11]=(cartesianBounds[5]-cartesianBounds[4])/2
        return matrix

def literal_to_geospatialTransform(literal: Literal) -> np.array:
    temp=str(literal)
    if 'None' not in temp:
        temp=temp.strip('[]')        
        res = list(map(float, temp.split(', ')))        
        return np.array([res[0],res[1],res[2]])
    else:
        return None  

def literal_to_cartesianBounds(literal: Literal)-> np.array:
    temp=str(literal)
    if 'None' not in temp:
        temp=str(literal)
        temp=temp.strip('[]')        
        res = list(map(float, temp.split(', ')))            
        return np.array([res[0],res[1],res[2],res[3],res[4],res[5]])
    else:
        return None  

def literal_to_float(literal: Literal) -> float:
    string=str(literal)
    if 'None' in string:
        return None
    else:
        return float(string)

def literal_to_string(literal: Literal)->str:
    string=str(literal)
    if 'None' in string:
        return None
    else:
        return string

def literal_to_list(literal: Literal)->list:
    string=str(literal)
    if 'None' in string:
        return None
    else: 
        return string_to_list(string)

def is_float(element) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False

def is_int(element) -> bool:
    try:
        int(element)
        return True
    except ValueError:
        return False

def is_uriref(element) -> bool:
    try:
        URIRef(element)
        return True
    except ValueError:
        return False

def is_string(element) -> bool:
    special_characters = "[!@#$%^&*()-+?_= ,<>/]'"
    if not any(c in special_characters for c in element):
        str(element)
        return True
    else:
        return False

def string_to_list(string:str)->list:
    """
    Convert string of items to a list of their respective types
    """
    string=string.strip("[!@#$%^&*()-+?_ =,<>]'")
    string=re.sub(' +', ' ',string)
    res=[]
    itemList=list(string.split(" "))
    for item in itemList:
        if is_float(item): 
            res.append(float(item))
        elif is_int(item): 
            res.append(int(item))
        elif is_string(item): 
            res.append(str(item))
        elif is_uriref(item): 
            res.append(URIRef(item))
    return res

def literal_to_int(literal: Literal) -> int:
    string=str(literal)
    if 'None' in string:
        return None
    else:
        return int(string)

def xml_to_float(xml) -> float:
    if xml is None:
        return None
    else:
        return float(xml)

def cartesianTransform_to_literal(matrix : np.array) -> str:
    """ convert nparray [4x4] to str([16x1])"""
    if matrix.size == 16: 
        return str(matrix.reshape(16,1))
    else:
        Exception("wrong array size!")    

def featured3d_to_literal(value) -> str:
    "No feature implementation yet"

def featured2d_to_literal(value) -> str:
    "No feature implementation yet"

def get_filename(path :str) -> str:
    """ Deconstruct path into filename"""
    path=ntpath.basename(path)
    head, tail = ntpath.split(path)
    array=tail.split('.')
    return array[0]

def get_folder(path :str) -> str:
    """ Deconstruct path and return forlder"""
    return os.path.dirname(os.path.realpath(path))

def get_timestamp(path : str) -> str:
    ctime=os.path.getctime(path)
    dtime=datetime.fromtimestamp(ctime).strftime('%Y-%m-%d %H:%M:%S')
    return dtime

def get_cartesian_bounds(geometry) ->np.array:
    """
    return array [min[0],max[0],min[1],max[1],min[2],max[2]]
    """
    max=geometry.get_max_bound()
    min=geometry.get_min_bound()
    return np.array([min[0],max[0],min[1],max[1],min[2],max[2]])
   
def lambert72_to_spherical_coordinates(x :float ,y:float) -> tuple: 
    """"
    Belgian Lambert 1972---> Spherical coordinates
    Input parameters : X, Y = Belgian coordinates in meters
    Output : latitude and longitude in Belgium Datum!
    source: http://zoologie.umons.ac.be/tc/algorithms.aspx
    """
    LongRef = 0.076042943  #      '=4°21'24"983
    nLamb  = 0.7716421928 #
    aCarre = 6378388 ^ 2 #
    bLamb = 6378388 * (1 - (1 / 297)) #
    eCarre = (aCarre - bLamb ^ 2) / aCarre #
    KLamb = 11565915.812935 #
    
    eLamb = math.Sqrt(eCarre)
    eSur2 = eLamb / 2
    
    Tan1  = (x - 150000.01256) / (5400088.4378 - y)
    Lambda = LongRef + (1 / nLamb) * (0.000142043 + math.Atan(Tan1))
    RLamb = math.Sqrt((x - 150000.01256) ^ 2 + (5400088.4378 - y) ^ 2)
    
    TanZDemi = (RLamb / KLamb) ^ (1 / nLamb)
    Lati1 = 2 * math.Atan(TanZDemi)
    
    eSin=0.0
    Mult1=0.0
    Mult2=0.0
    Mult=0.0
    LatiN=0.0
    Diff=1     

    while math.Abs(Diff) > 0.0000000277777:
        eSin = eLamb * math.Sin(Lati1)
        Mult1 = 1 - eSin
        Mult2 = 1 + eSin
        Mult = (Mult1 / Mult2) ^ (eLamb / 2)
        LatiN = (math.PI / 2) - (2 * (math.Atan(TanZDemi * Mult)))
        Diff = LatiN - Lati1
        Lati1 = LatiN
    
    latBel = (LatiN * 180) / math.PI
    lngBel = (Lambda * 180) / math.PI
    return latBel,lngBel

def spherical_coordinates_to_lambert72(latBel :float,lngBel:float) -> tuple:
    """
    Conversion from spherical coordinates to Lambert 72
    Input parameters : lat, lng (spherical coordinates)
    Spherical coordinates are in decimal degrees converted to Belgium datum!
    source: http://zoologie.umons.ac.be/tc/algorithms.aspx
    """
 
    LongRef  = 0.076042943  #      '=4°21'24"983
    bLamb  = 6378388 * (1 - (1 / 297))
    aCarre  = 6378388 ^ 2
    eCarre = (aCarre - bLamb ^ 2) / aCarre
    KLamb = 11565915.812935
    nLamb = 0.7716421928
    
    eLamb  = math.Sqrt(eCarre)
    eSur2  = eLamb / 2
    
    #conversion to radians
    lat = (math.PI / 180) * latBel
    lng = (math.PI / 180) * lngBel
    
    eSinLatitude = eLamb * math.Sin(lat)
    TanZDemi = (math.Tan((math.PI / 4) - (lat / 2))) *  (((1 + (eSinLatitude)) / (1 - (eSinLatitude))) ^ (eSur2))
    
    RLamb= KLamb * ((TanZDemi) ^ nLamb)
    
    Teta  = nLamb * (lng - LongRef)
        
    x = 150000 + 0.01256 + RLamb * math.Sin(Teta - 0.000142043)
    y = 5400000 + 88.4378 - RLamb * math.Cos(Teta - 0.000142043)
    return x,y

def belgian_datum_to_wgs84(latBel:float,lngBel:float) -> tuple:
    """
    Input parameters : Lat, Lng : latitude / longitude in decimal degrees and in Belgian 1972 datum
    Output parameters : LatWGS84, LngWGS84 : latitude / longitude in decimal degrees and in WGS84 datum
    source: http://zoologie.umons.ac.be/tc/algorithms.aspx
    """
    Haut = 0.0   
        
    #conversion to radians
    Lat = (math.PI / 180) * latBel
    Lng = (math.PI / 180) * lngBel
    
    SinLat = math.Sin(Lat)
    SinLng = math.Sin(Lng)
    CoSinLat = math.Cos(Lat)
    CoSinLng = math.Cos(Lng)
    
    dx = -125.8
    dy = 79.9
    dz = -100.5
    da = -251.0
    df = -0.000014192702
    
    LWf = 1 / 297
    LWa = 6378388
    LWb = (1 - LWf) * LWa
    LWe2 = (2 * LWf) - (LWf * LWf)
    Adb = 1 / (1 - LWf)
    
    Rn = LWa / math.Sqrt(1 - LWe2 * SinLat * SinLat)
    Rm = LWa * (1 - LWe2) / (1 - LWe2 * Lat * Lat) ^ 1.5
    
    DLat = -dx * SinLat * CoSinLng - dy * SinLat * SinLng + dz * CoSinLat
    DLat = DLat + da * (Rn * LWe2 * SinLat * CoSinLat) / LWa
    DLat = DLat + df * (Rm * Adb + Rn / Adb) * SinLat * CoSinLat
    DLat = DLat / (Rm + Haut)
    
    DLng = (-dx * SinLng + dy * CoSinLng) / ((Rn + Haut) * CoSinLat)
    Dh = dx * CoSinLat * CoSinLng + dy * CoSinLat * SinLng + dz * SinLat
    Dh = Dh - da * LWa / Rn + df * Rn * Lat * Lat / Adb
    
    LatWGS84 = ((Lat + DLat) * 180) / math.PI
    LngWGS84 = ((Lng + DLng) * 180) / math.PI
    return LatWGS84,LngWGS84

def wgs84_to_belgian_datum(LatWGS84: float,LngWGS84:float) -> tuple:
    """
    Input parameters : Lat, Lng : latitude / longitude in decimal degrees and in WGS84 datum
    Output parameters : LatBel, LngBel : latitude / longitude in decimal degrees and in Belgian datum
    source: http://zoologie.umons.ac.be/tc/algorithms.aspx
    """
    Haut = 0    
    
    #conversion to radians
    Lat = (math.PI / 180) * LatWGS84
    Lng = (math.PI / 180) * LngWGS84
    
    SinLat = math.Sin(Lat)
    SinLng = math.Sin(Lng)
    CoSinLat = math.Cos(Lat)
    CoSinLng = math.Cos(Lng)
    
    dx = 125.8
    dy = -79.9
    dz = 100.5
    da = 251.0
    df = 0.000014192702
    
    LWf = 1 / 297
    LWa = 6378388
    LWb = (1 - LWf) * LWa
    LWe2 = (2 * LWf) - (LWf * LWf)
    Adb = 1 / (1 - LWf)
    
    Rn = LWa / math.Sqrt(1 - LWe2 * SinLat * SinLat)
    Rm = LWa * (1 - LWe2) / (1 - LWe2 * Lat * Lat) ^ 1.5
    
    DLat = -dx * SinLat * CoSinLng - dy * SinLat * SinLng + dz * CoSinLat
    DLat = DLat + da * (Rn * LWe2 * SinLat * CoSinLat) / LWa
    DLat = DLat + df * (Rm * Adb + Rn / Adb) * SinLat * CoSinLat
    DLat = DLat / (Rm + Haut)
    
    DLng = (-dx * SinLng + dy * CoSinLng) / ((Rn + Haut) * CoSinLat)
    Dh = dx * CoSinLat * CoSinLng + dy * CoSinLat * SinLng + dz * SinLat
    Dh = Dh - da * LWa / Rn + df * Rn * Lat * Lat / Adb
    
    LatBel = ((Lat + DLat) * 180) / math.PI
    LngBel = ((Lng + DLng) * 180) / math.PI
    return  LatBel,LngBel

def getListOfFiles(directoryPath:str) -> list:
    """Get a list of all files in the directory and subdirectories

    Args:
        directoryPath: directory path e.g. "D:\\Data\\2018-06 Werfopvolging Academiestraat Gent\\week 22\\"
            
    Returns:
        A list of files 
    """
    # names in the given directory 
    listOfFile = os.listdir(directoryPath)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(directoryPath, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)                
    return allFiles

def clean_attributes_list(list:list) -> list:
    #NODE
    if 'graph' in list:
        list.remove ('graph')
    if 'name' in list:
        list.remove ('name')
    if 'graphPath' in list:
        list.remove ('graphPath')    
    # if 'path' in list:
    #     list.remove ('path')    
    #BIMNODE
    if 'ifcElement' in list:
        list.remove ('ifcElement')
    #IMGNODE
    if 'exifData' in list:
        list.remove ('exifData')
    if 'img' in list:
        list.remove ('img')
    #MESHNODE
    if 'mesh' in list:
        list.remove ('mesh') 
    #PCDNODE
    if 'pcd' in list:
        list.remove ('pcd')
    if 'e57Pointcloud' in list:
        list.remove ('e57Pointcloud')
    if 'e57xmlNode' in list:
        list.remove ('e57xmlNode')
    if 'e57image' in list:
        list.remove ('e57image')
    return list

def save_graph(graph, graphpath) -> None:
        with open(graphpath, 'w') as f:
            f.write(graph.serialize())
