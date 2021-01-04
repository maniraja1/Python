from setup import db_mssql
from helper import AuditQuery

class Audit:

    def __init__(self, auditid, debug=False):

        self.auditid = auditid
        self._audit = self.GetAudit()
        self.sourcequery = self._audit[0]['sourcequery']
        self.targetquery = self._audit[0]['targetquery']
        self._debug = debug

    @property
    def auditid(self):
        return self.__auditid

    @auditid.setter
    def auditid(self, value):
        self.__auditid = value

    @property
    def sourcequery(self):
        return self.__sourcequery

    @sourcequery.setter
    def sourcequery(self, value):
        self.__sourcequery = value

    @property
    def targetquery(self):
        return self.__targetquery

    @targetquery.setter
    def targetquery(self, value):
        self.__targetquery = value

    def GetAudit(self):
        with db_mssql.connect() as connection:
            audit_row = connection.execute(f"select auditid, sourcequery, targetquery from audits"
                                           f" where auditid = {self.auditid}")
            audit_dict = ([(dict(row.items())) for row in audit_row])
            return audit_dict

    def RunAudit(self):
        source = AuditQuery(self.sourcequery, self._debug).executefile()
        target = AuditQuery(self.targetquery, self._debug).executefile()
        if self._debug:
            print(source)
            print(target)
        if source == target:
            print(f"AuditID: {self.auditid}, Result: Successful")
        else:
            print(f"AuditID: {self.auditid}, Result: Failure")






'''
a = audit(1)
print(a.sourcequery)'''



