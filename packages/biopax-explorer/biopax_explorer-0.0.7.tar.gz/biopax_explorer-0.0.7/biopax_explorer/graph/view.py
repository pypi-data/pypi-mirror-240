from biopax_explorer.biopax.utils import gen_utils as gu
import  rdfobj  as ro 

import networkx as nx


          
class GraphModelLayer(ro.GraphModelLayer):
    """
    
    """
    def __init__(self):
     
         super().__init__() 
         super().build(gu)


class Factory():
    def __init__(self,back="NX"):
        self.glayer=None
        self.has_gt=None

        if back=="NK":
          self.glayer= GraphDatasetLayerNX()
        elif  back=="GT":   
          
          
          try:
             import  graph_tool.all as gt
             self.has_gt=True
             self.glayer= GraphDatasetLayerGT()
          except:
            self.has_gt=False
            print("WARNING: The package graph-tool is not installed. GraphDatasetLayerGT can not be instancied ")
            self.glayer=None
          
        else:
          self.glayer= GraphDatasetLayerNX()    
    def graphDatasetLayer(self):
        return self.glayer
          

class GraphDatasetLayerNX(ro.GraphDatasetLayerAbs):
    """
    
    """
    def __init__(self):
      
         super().__init__()          
         self.mpop=gu.modelPopulator()
         self.model_instance_dict={} 

    def populate_dataset(self,db,dataset):
        dburl=db+"/%s/query"
        self.model_instance_dict=self.mpop.populate_domain_instance(dburl,dataset,gu.prefix(),gu.domain()) 


class GraphDatasetLayerGT(ro.GraphDatasetLayerAbsBKGT):
    """
    
    """
    def __init__(self):
      
         super().__init__()          
         self.mpop=gu.modelPopulator()
         self.model_instance_dict={} 

    def populate_dataset(self,db,dataset):
        dburl=db+"/%s/query"
        self.model_instance_dict=self.mpop.populate_domain_instance(dburl,dataset,gu.prefix(),gu.domain()) 
       



################


