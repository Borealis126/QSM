import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("fullS21")
oDesign = oProject.SetActiveDesign("Netlist")
oModuleReport = oDesign.GetModule("ReportSetup")
oDesign.AnalyzeAll()
oModuleReport.CreateReport("S Parameter Table 1", "Standard", "Data Table", "LNA",
    [
        "NAME:Context",
        "SimValueContext:="	, [3,0,2,0,False,False,-1,1,0,1,1,"",0,0]
    ],
    [
        "F:="			, ["All"]
    ],
    [
        "X Component:="		, "F",
        "Y Component:="		, ["S(2,1)"]
    ], [])
oModuleReport.ExportToFile("S Parameter Table 1", "/beegfs/scratch/joelhoward/QSMSimulations/QSMTests/SWIFT500um/fullS21/fullS21_Results.csv", False)
oProject.Save()
