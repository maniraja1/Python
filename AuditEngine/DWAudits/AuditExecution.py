from setup import db_mssql
from Audits import Audit

class AuditExecution:

    def __init__(self, debug=False):
        self._debug = debug
        self.Audits = self.get_all_audits()



    def get_all_audits(self):
        with db_mssql.connect() as connection:
            auditexec = connection.execute(f"select auditid  from audits")
            auditexec_list = [Audit((dict(row.items()))['auditid'], self._debug) for row in auditexec]
            return auditexec_list

    def eval_all_audits(self):
        for x in self.Audits:
            if self._debug:
                print(x.auditid, x.sourcequery, x.targetquery)
            x.RunAudit()


ae = AuditExecution()
ae.eval_all_audits()

