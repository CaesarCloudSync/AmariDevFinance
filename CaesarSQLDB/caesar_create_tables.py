class CaesarCreateTables:
    def __init__(self) -> None:
        self.amarifinancepotsfields = ("potinfo",)

        

    def create(self,caesarcrud):
        caesarcrud.create_table("potid",self.amarifinancepotsfields,
        ("TEXT NOT NULL",),
        "amarifinancepots")
