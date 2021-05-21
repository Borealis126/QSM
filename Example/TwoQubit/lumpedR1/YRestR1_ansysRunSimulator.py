import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("YRestR1")
oDesign = oProject.SetActiveDesign("Netlist")
oModuleReport = oDesign.GetModule("ReportSetup")
oDesign.AnalyzeAll()
oModuleReport.CreateReport("Y Parameter Table 1", "Standard", "Data Table", "LNA",
    [
        "NAME:Context",
        "SimValueContext:="	, [3,0,2,0,False,False,-1,1,0,1,1,"",0,0]
    ],
    [
        "F:="			, ["All"]
    ],
    [
        "X Component:="		, "F",
        "Y Component:="		, ["Y(1,1)"]
    ], [])
oModuleReport.ExportToFile("Y Parameter Table 1", r"/beegfs/scratch/joelhoward/QSMSimulations/QSMSource/Example/TwoQubit/lumpedR1/YRestR1_Results.csv", False)
oProject.Save()
