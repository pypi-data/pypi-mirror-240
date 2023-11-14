import os,pathlib

from SPARQLWrapper import SPARQLWrapper, JSON, POST, DIGEST
import networkx as nx
 
 

import textwrap

from rdfobj import *
import rdfobj
from biopax_explorer.biopax.utils import gen_utils as gu
from biopax_explorer.biopax  import *
from biopax_explorer.graph  import serializer as se

class BIOPAXStoreClient():
  def __init__(self,db,dataset,credentials=None,unwanted_subject_uri=None):
  
     self.prefix=gu.prefix()
     self.domain_schema_uri=gu.domain()
     self.mp=gu.modelPopulator()
     classDict=self.mp.classDict
     self.sc=StoreClient(classDict) 
     self.db=db
     self.dataset=dataset
     self.credentials=credentials 
     urlq=self.dbstr(self.db,self.route_query(self.dataset)) 
     self.wrapper_query=self.defineWrapper(urlq,self.credentials)
     urlu=self.dbstr(self.db,self.route_update(self.dataset)) 
     self.wrapper_update=self.defineWrapper(urlu,self.credentials) 
     self.unwanted_subject_uri=unwanted_subject_uri 
  
  def dbstr(self,pre,sfx):        
    return "%s/%s" %(pre,sfx)


  def route_update(self, path):
      return "%s/%s" %(path,"update")
      
  def route_query(self,path):    
       return "%s/%s" %(path,"query")
      
  def defineWrapper(self,url,credentials): 
      
      wrapper = SPARQLWrapper(url)
      
      wrapper.setMethod('POST')
      wrapper.setReturnFormat(JSON)
      if credentials is not None:
         wrapper.setCredentials(credentials[0], credentials[1])
      
      return wrapper
      

  def executeQuery(self,query): 
       dbstr=self.dbstr(self.db,self.route_query(self.dataset))
       results=self.mp.executeQuery(dbstr, None,query)
       
       return results
      
  def execute(self,query) :
      lst=[]
       
             
      results=self.executeQuery(query) 
      heads=results["head"]["vars"]
      bindings=results["results"]["bindings"]
    
      if len(bindings)==0:
         return lst
      
      for result in bindings:
        tp=[]
        for v in heads:
           tp.append(result[v]['value'])
        lst.append(tp)  
      return lst

    
  def define_bp_template(self):

   return se.bp_template()
  
  def store_to_graph(self,limit=1000):
      dbstr=self.dbstr(self.db,self.route_query(self.dataset))
      print(dbstr,self.prefix,self.domain_schema_uri,self.unwanted_subject_uri,limit)
      g=self.sc.store_to_graph(dbstr,self.prefix,self.domain_schema_uri,self.unwanted_subject_uri,limit)
      return g
       
  def save_graph_as_rdf_xml(self,efile, gr=None):   
      g=self.sc.save_graph_as_rdf_xml(efile, gr)   
      return g


  def custom_query_list_append(self,q):
      return self.sc.custom_query_list.append(q)
       
  def store_custom_query_to_graph(self,extension, labels=None):  
      dbstr=self.dbstr(self.db,self.route_query(self.dataset))
      if labels is None:
        return self.sc.store_custom_query_to_graph(dbstr,extension)
      else:
        return self.sc.store_custom_query_to_graph(dbstr,extension, labels) 
      
  def delete_from_store_by_uri_id(self,uri_id,prefix=None,domain=None):
      if prefix is None:
          prefix=self.prefix
      if domain is None:
          domain=self.domain
          
      return self.sc.delete_from_store_by_uri_id(self.wrapper_update,uri_id, prefix, domain)

  def insert_instance(self,rel):
      return self.sc.insert_instance(self.wrapper_update,rel)
      
  def update_or_insert_instance(self,rel):
      return self.sc.update_or_insert_instance(self.wrapper_update,rel)

  def select_all_query(self,limit=1000,offset=0):
      return self.sc.select_all_query(self.prefix,self.domain_schema_uri,self.unwanted_subject_uri,limit,offset)

  def file_to_graph(self,file) :
      return self.sc.file_to_graph(file)

  def string_to_graph(self,xml) :
     return self.sc.string_to_graph(xml)
  
  def rdf_xml_string(self,g=None): 
      return self.sc.rdf_xml_string(g)

  def nxgraph(self,g=None):
    # Create an empty NetworkX graph
    nx_graph = nx.Graph()
    if g is None:
      rdf_graph=self.sc.g
    else:
      rdf_graph=g   
    # Iterate through RDF triples and add nodes and edges to NetworkX graph
    for subject, predicate, obj in rdf_graph:
        subject_node = str(subject)
        object_node = str(obj)
        predicate_edge = str(predicate)
        nx_graph.add_node(subject_node)
        nx_graph.add_node(object_node)
        nx_graph.add_edge(subject_node, object_node, predicate=predicate_edge)
    return nx_graph

