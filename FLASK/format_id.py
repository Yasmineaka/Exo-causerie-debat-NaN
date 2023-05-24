def id(d):
        cp=dict.copy(d)
        cp['_id']=str(d['_id'])
        return cp
def convert(cursor):
    ls=list(cursor)
    ls = list(map(id,ls))
    return ls