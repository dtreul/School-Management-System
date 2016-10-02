from google.appengine.ext import ndb
import endpoints
import json




def getEntityDic(entityID, entityName):
    key = ndb.Key(entityName, entityID)
    entity = key.get()
    if entity is None:
        return {}
    else:
        return entity.to_dict()
    
def getEntity(entityID, entityName):
    '''
    input: entityID: int, entityName: string ('Student', 'Instructor', etc...)
    output: JSON string of entity
    '''
    dic = getEntityDic(entityID, entityName)
    return json.dumps(dic, indent=4, sort_keys=True)


def putEntity(entity):
    '''
    puts entity into datastore
    '''
    entity.key = ndb.Key(entity.name, entity.idNumber)
    entity.put()

def postEntity(entityID, entityName, dic):
    '''
    inputs: entityID: int, entityName: string ('Student', 'Instructor', etc..), dic: dictionary of things to be overwritten
    updates entity in datastore with new key value pairs in dict
    '''
    key = ndb.Key(entityName, entityID)
    entity = key.get()
    if entity is None:
        message = 'No entity with the id "%s" exists.' % entityID
        raise endpoints.NotFoundException(message)
        
    entityAttributes = entity.to_dict().keys()
    for key in dic:
        if key not in entityAttributes:
            break
        else:
            if key is "idNumber":
                entity.id = dic[key]    
            setattr(entity, key, dic[key])
    entity.put()
    
def deleteEntity(entityID, entityName):
    key = ndb.Key(entityName, entityID)
    key.delete()
    
def entityStringer(entity):
    '''
    returns json of entity
    '''
    return json.dumps(entity.to_dict(), indent=4, sort_keys=True)


def getAllEntities(entityClass):
    '''
    returns json of all entities
    '''
    outString = entityClass.name
    outString += ': [\n'
    for entity in entityClass.query().fetch():
        outString += entityStringer(entity)
        outString += ','
    outString = outString[:-1] + '\n]'
    return outString