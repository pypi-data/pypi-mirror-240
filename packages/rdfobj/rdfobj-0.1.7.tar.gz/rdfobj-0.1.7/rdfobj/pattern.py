 
from .query import QueryBuilder 
 
from .toolbox_sparql import Toolbox
from .mapper import ModelPopulator
from .query_utils import uniqueEntities,entitiesDict, is_listoflist

from .utils import constantDict

import copy

from rdflib.namespace import   RDF

#pattern container class . owns a sequence of  elements
# each one  enables :
# #1/ sparql query  generation 
# 2/ or local processing on entities

class Pattern():
    
    def __init__(self):
      self.processing_step: list[Step] = []
      self.description=""

    def definePostPump(self,level):
       if self.processing_step is not None and len(self.processing_step)>0:
         lix=len(self.processing_step)-1
         laststep=self.processing_step[lix]
         if  isinstance(laststep.core,DataPump)==False:
            dpstep = Step(DataPump(level))
            self.processing_step.append(dpstep)
         

    def byReference(self, do_pk_only=True):
       #risky
       for step in self.processing_step:
          step.do_pk_only=do_pk_only

       
    def define(self, *args):
      """shortcut to simplify the  usage of processing steps
      """
      self.processing_step=[]
      lst=[]
      for a in args:
        lst.append(a)
      step_1=  Step(lst)
      step_1.do_pk_only = True
      step_1.do_tuple_result = True # Not necessary
      self.processing_step.append(step_1)
              
class LocalProcessing():
    
    def __init__(self):
      self.method = None
      self.parameters = {}

class DataPump():
    def __init__(self,level=1):
      self.method = None     
      self.level=level # iteration number to extend collection using association  

# a step is a part of the sequence of a Pattern
class Step():
    def __init__(self,core, add_children = True, op="UNION"):
      self.operator = op
      self.core=core
      self.add_children = add_children
      self.do_pk_only=False # only  for sparql queries, If Thrue, only uri  and class is extracted and an instance of class PK is created
      # then a DataPump is needed at the end of the pattern to fill the entities
      self.do_tuple_result=False #if True,  model populator must output a list of lists and not list, usefull for some following localprocessing 


    





class PatternExecutor():
    
  def __init__(self,gen_utils,db,dataset,blacklist=None,doProcess=True):
      
      self.gen_utils=gen_utils
      self.mpop: ModelPopulator=gen_utils.modelPopulator()
      self.db=None
      self.dataset=None 
      self.glist=[]
      if db is None:
             self.fromFile=True
      else:
         self.fromFile=False
         self.db="%s/%s/query" %(db, dataset)
         self.dataset=None


      self.alias=gen_utils.shortPrefix()
      self.uri=gen_utils.domain()
      self.doProcess=doProcess
      self.blacklist=blacklist
      self.querylist=[]
      self.vmeta=[]
      self.lastml=None
      self.do_debug=False
      self.processed_steps=None
      self.trace=[]

  def verbose(self,verb=True):
      self.do_debug=verb

  #testing purpose limit the number o fresults
  def maxCount(self,mcount):
     self.mpop.max_count=mcount

  #internal limit for example: max count of attributes related to one single instance
  def limit(self,climit):
     self.mpop.limit=climit

  def datasetFile(self,dataset_file):
    """_define the source rdf/xml file touse as a in memory graph
    Args:
        dataset_file (_type_): xml rdf file path
    """
    self.mpop.dataset_file=dataset_file

  def createQueryBuilder(self, add_children: bool = True):
    
    alias=self.alias
    uri=self.uri
 

    tb=Toolbox(alias,uri,self.gen_utils) 
    queryBuilder=QueryBuilder()
    queryBuilder.add_children=add_children

    queryBuilder.addToolBox(tb)
    return  queryBuilder

  def steplog(self,*msg):
     self.log(msg)
     self.trace.append(msg)

  def log(self,*msg):
     if self.do_debug:
        print("debug: ",msg)

  def validate_processed_steps(self) -> bool:
     return all(s.do_tuple_result for s in self.processed_steps)
  
  


  def queries(self,p:Pattern):
      self.querylist=[]
      self.vmeta=[]
      self.executePatternImpl(p, True)   
      return self.querylist

   
  def fetchEntities(self,p:Pattern, level=1,max_count=None):
     pc=copy.deepcopy(p)
     pc.definePostPump(level)
     return self.executePattern(pc,None, max_count=max_count)

  def executePattern(self,p:Pattern,by_reference=None, max_count=None):
      
      if by_reference is not None:
          # we force the pattern by_reference
          p.byReference(by_reference)
      if max_count is not None:
          # we force the maximum  number of results
          self.maxCount(max_count)

      self.querylist=[]
      self.vmeta=[]
      rsl= self.executePatternImpl(p, False) 
      if rsl is not None and isinstance(rsl,list)==False:
         rsl=[rsl]  
      return rsl
  
  def executePatternImpl(self,p:Pattern, simul):
   self.glist=[]
   self.trace=[]
   resultFinal=[] # entities collection from the  BIOPAX python model
   self.processed_steps:list[Step] = []
   stepcount=0
   nb_step = len(p.processing_step)
   for step in p.processing_step:
     #print(step)
     stepcount+=1
     self.steplog(f"STEP N°{stepcount}/{nb_step}")
     if isinstance(step.core,list):
       self.log("SparqlQuery:",step.core) 
       ##
       if self.doProcess==True: 
         
         
         queryBuilder=self.createQueryBuilder(step.add_children)  
         enl=step.core
         queryBuilder.add(enl)
         query=queryBuilder.sparql_generate() 
         self.glist.append(queryBuilder.g)
         self.log("#\n",query,"\n#")
         self.querylist.append(query)
         vmetadata=queryBuilder.variable_metadata() 
         self.vmeta.append(vmetadata)  
         self.log(f"VMETADATA = {vmetadata}")
         if simul==False:
            resultQ = self.executeSparqlQuery(query,vmetadata,step.do_pk_only, step.do_tuple_result) # return  instances of biopax classes
         else:
            resultQ =[]

         self.log(f"RESULTQ = {resultQ}")
         #intersect or union or difference
         resultFinal=self.operatorProcess(step.operator,resultQ,resultFinal)
         self.log("RESULT SparqlQuery after%s  STEP %s, LENGTH= %s" %(step.operator,stepcount,len(resultFinal)))
         for el in resultFinal:
           self.log(f" -> {el}")
         self.testType(resultFinal,"sparql")
        
     elif  isinstance(step.core,LocalProcessing):
       if step.do_tuple_result and not self.validate_processed_steps():
          raise Exception("All the results from precent steps has to be tuple")
       ##
       self.log("LocalProcessing:",step.core) 
       if self.doProcess==True: 
         lp=step.core
         #step.validateLocalProcessing()
         resultFinal= self.executeLocalProcessing(lp,resultFinal) # return  instances of biopax classes # ex get_res refactored(...)
         self.testType(resultFinal,"localp")
     elif  isinstance(step.core,DataPump):
       ##
       self.log("DataPump:",step.core) 
       if self.doProcess==True:
         #print("do_pump:1") 
         dp=step.core

         resultFinal= self.pump(resultFinal,dp.level)
         self.testType(resultFinal,"pump")
     self.processed_steps.append(step)
     self.log("End of the step.")
     self.steplog(f"SIZE OF RESULT : {len(resultFinal)}")
   return resultFinal
  
  def testType(self,res,tag):
     for el in res:
        if isinstance(el,list):
           self.log(" element 1 %s is a list , step: %s" %(el,tag))
        else:
           self.log(" element 1 %s is an entity or pk , step: %s" %(el,tag))
        break
     
  def executeLocalProcessing(self, lp:LocalProcessing, inputCollection):
      
      # we populate collection with the current list of entities
      lp.parameters['collection']=inputCollection
      # lp.parameters['tuple_input']=self.laststep.do_tuple_result # type of this provided inputCollection

      outputCollection=lp.method(lp.parameters)
      return outputCollection
  def pump(self, resultFin,level=1):
      #resultFin: list of list (of PK())
      inputInstDict=dict()# a simple map pk-> full entity
      for elm in resultFin:
           if isinstance(elm,list):
              for el in elm:
                 inputInstDict[el.pk]=el
           else:   
             inputInstDict[elm.pk]=elm
         #print("do_pump:2") 

      outputInstFullDict=self.pumpImpl( inputInstDict,level)
      ofd={}
      for k in outputInstFullDict:
        ofd[k.pk]=k

      resFinFull=[]
      for ell in resultFin:
         row=[]
         if isinstance(ell,list):
             ellst=ell
         else:
             ellst=[ell]

         for ent_pk in ellst:
            pk=ent_pk.pk
            if pk in ofd.keys():
               ent_full=ofd[pk]
            else:
               ent_full= ent_pk # should never append (can be used to complete progressivly ?)
            row.append(ent_full)
         resFinFull.append(row)
      return resFinFull

  def pumpImpl(self, inputInstDict,level=1):
      
       # we complete the attributes of the already selected entities
       ml=self.lastml 
        
       type_uri=None
       do_populate_asso=True
       self.log("-executePump--start")
       #print("-executePump--start")
       collec=self.mpop.executePump(self.db,self.dataset,inputInstDict, ml,self.alias ,self.uri,type_uri,do_populate_asso ,level)
       self.log("-executePump--end")  
       #print("-executePump--end")
       entities=[]
       for uri,element in collec.items():
         #self.log("%s=>%s" %(uri,element.to_json()))
         entities.append(element)
         #print(element)
       return entities
  
      

  def operatorProcess(self,op,resultQ,resultFinal):
    
     
     if op=="UNION":
        resultFinal=self.union(resultQ,resultFinal)       
     elif op=="INTERSECTION":       
        resultFinal=self.intersection(resultQ,resultFinal)       
     elif op=="DIFFERENCE":       
        resultFinal=self.difference(resultQ,resultFinal)     
     
     return resultFinal



  def union(self,part,col):
        col.extend(part)
        # If col is of type list[list] then, it will return col.
        if is_listoflist(col):
           return col
        else:
          ue=uniqueEntities(col)
          return ue
    
  def intersection(self,part,col):
        
 
        s1 = set()
        s2 = set()
        for el in part:
            s1.add(el.pk)
        for el in col:
            s2.add(el.pk)
            
        entities=dict()    
        inter=s1.intersection(s2)
        ed=entitiesDict(part)
        for pk in inter:
            if pk in ed.keys():
                entities.append(ed[pk])
                
        return entities        

  def difference(self,part,col):
   
        s1 = set()
        s2 = set()
        for el in part:
            s1.add(el.pk)
        for el in col:
            s2.add(el.pk)
            
        entities=dict()    
        diff=s1.difference(s2)
        ed=entitiesDict(part)
        for pk in diff:
            if pk in ed.keys():
                entities.append(ed[pk])
                
        return entities
  

  def executeSparqlQuery(self,query,ml,do_pk_only=False, tuple_result: bool = False) -> list:
    #self.log("==>ml:",ml)
    self.lastml=ml
    collec=self.mpop.executeCustomQuery(self.db,self.dataset,query, ml,self.alias ,self.uri,do_pk_only, tuple_result)
    self.log(f"{collec =}")
    if tuple_result:
      return collec
    else:
      entities=[]
      for uri,element in collec.items():
        self.log("%s\n" %( element))
        entities.append(element)
      
      return entities



