def id(d):
        cp=dict.copy(d)
        cp['_id']=str(d['_id'])
        return cp
def convert(cursor):
    ls=list(cursor)
    ls = list(map(id,ls))
    return ls

def from_objectId_to_json(document):
      user= user.to_json()
      cp = dict.copy(document)
      cp["_id"]=cp['_id']['$oid']
      return cp