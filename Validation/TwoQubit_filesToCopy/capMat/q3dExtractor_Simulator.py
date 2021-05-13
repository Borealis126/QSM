import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("q3dExtractor")
oProject.InsertDesign("Q3D Extractor", "q3dExtractor", "", "")
oDesign = oProject.SetActiveDesign("q3dExtractor")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oModuleBoundary = oDesign.GetModule("BoundarySetup")
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-4750.0um",
                "Y:="			, "-3750.0um",
                "Z:="			, "0um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-4750.0um",
                "Y:="			, "3750.0um",
                "Z:="			, "0um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "4750.0um",
                "Y:="			, "3750.0um",
                "Z:="			, "0um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "4750.0um",
                "Y:="			, "-3750.0um",
                "Z:="			, "0um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-4750.0um",
                "Y:="			, "-3750.0um",
                "Z:="			, "0um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "S0",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "S0",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "500um",
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-4750.0um",
                "Y:="			, "-3750.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-4750.0um",
                "Y:="			, "3750.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "4750.0um",
                "Y:="			, "3750.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "4750.0um",
                "Y:="			, "-3750.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-4750.0um",
                "Y:="			, "-3750.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "G0",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-581.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-581.0um",
                "Y:="			, "-299.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-81.0um",
                "Y:="			, "-299.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-81.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-329.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-329.0um",
                "Y:="			, "-450.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-333.0um",
                "Y:="			, "-450.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-333.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-581.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oModuleBoundary.AssignThinConductor(
    [
        "NAME:ThinCondQ0Pad1",
        "Objects:="		, ["Q0Pad1"],
        "Material:="		, "perfect conductor",
        "Thickness:="		, "0.1um"
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-581.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-581.0um",
                "Y:="			, "-299.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-81.0um",
                "Y:="			, "-299.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-81.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-329.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-329.0um",
                "Y:="			, "-450.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-333.0um",
                "Y:="			, "-450.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-333.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-581.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad1TrenchComponent",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-681.0um",
                "Y:="			, "-539.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-681.0um",
                "Y:="			, "-199.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "19.0um",
                "Y:="			, "-199.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "19.0um",
                "Y:="			, "-539.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-681.0um",
                "Y:="			, "-539.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad1TrenchPeriphery0",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-363.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-299.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad1TrenchPeriphery1",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q0Pad1TrenchPeriphery0",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "Q0Pad1TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q0Pad1TrenchPeriphery1",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "Q0Pad1TrenchPeriphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q0Pad1",
        "Objects:="		, ["Q0Pad1"]
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-681.0um",
                "Y:="			, "-539.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-681.0um",
                "Y:="			, "-199.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "19.0um",
                "Y:="			, "-199.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "19.0um",
                "Y:="			, "-539.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-681.0um",
                "Y:="			, "-539.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad1periphery0",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "Q0Pad1periphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-363.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-299.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad1periphery1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "Q0Pad1periphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-81.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-81.0um",
                "Y:="			, "-609.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-581.0um",
                "Y:="			, "-609.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-581.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-333.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-333.0um",
                "Y:="			, "-458.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-329.0um",
                "Y:="			, "-458.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-329.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-81.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad2",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oModuleBoundary.AssignThinConductor(
    [
        "NAME:ThinCondQ0Pad2",
        "Objects:="		, ["Q0Pad2"],
        "Material:="		, "perfect conductor",
        "Thickness:="		, "0.1um"
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-81.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-81.0um",
                "Y:="			, "-609.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-581.0um",
                "Y:="			, "-609.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-581.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-333.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-333.0um",
                "Y:="			, "-458.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-329.0um",
                "Y:="			, "-458.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-329.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-81.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad2TrenchComponent",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "19.0um",
                "Y:="			, "-369.00000000000006um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "19.0um",
                "Y:="			, "-709.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-681.0um",
                "Y:="			, "-709.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-681.0um",
                "Y:="			, "-368.99999999999994um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "19.0um",
                "Y:="			, "-369.00000000000006um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad2TrenchPeriphery0",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-299.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-363.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad2TrenchPeriphery1",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q0Pad2TrenchPeriphery0",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "Q0Pad2TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q0Pad2TrenchPeriphery1",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "Q0Pad2TrenchPeriphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q0Pad2",
        "Objects:="		, ["Q0Pad2"]
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "19.0um",
                "Y:="			, "-369.00000000000006um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "19.0um",
                "Y:="			, "-709.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-681.0um",
                "Y:="			, "-709.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-681.0um",
                "Y:="			, "-368.99999999999994um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "19.0um",
                "Y:="			, "-369.00000000000006um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad2periphery0",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "Q0Pad2periphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-299.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-363.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad2periphery1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "Q0Pad2periphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "81.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "81.0um",
                "Y:="			, "-301.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "581.0um",
                "Y:="			, "-301.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "581.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "333.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "333.0um",
                "Y:="			, "-450.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "329.0um",
                "Y:="			, "-450.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "329.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "81.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oModuleBoundary.AssignThinConductor(
    [
        "NAME:ThinCondQ1Pad1",
        "Objects:="		, ["Q1Pad1"],
        "Material:="		, "perfect conductor",
        "Thickness:="		, "0.1um"
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "81.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "81.0um",
                "Y:="			, "-301.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "581.0um",
                "Y:="			, "-301.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "581.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "333.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "333.0um",
                "Y:="			, "-450.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "329.0um",
                "Y:="			, "-450.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "329.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "81.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad1TrenchComponent",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-19.0um",
                "Y:="			, "-521.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-19.0um",
                "Y:="			, "-199.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "681.0um",
                "Y:="			, "-199.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "681.0um",
                "Y:="			, "-521.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-19.0um",
                "Y:="			, "-521.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad1TrenchPeriphery0",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "299.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "363.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad1TrenchPeriphery1",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q1Pad1TrenchPeriphery0",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "Q1Pad1TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q1Pad1TrenchPeriphery1",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "Q1Pad1TrenchPeriphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q1Pad1",
        "Objects:="		, ["Q1Pad1"]
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-19.0um",
                "Y:="			, "-521.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-19.0um",
                "Y:="			, "-199.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "681.0um",
                "Y:="			, "-199.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "681.0um",
                "Y:="			, "-521.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-19.0um",
                "Y:="			, "-521.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad1periphery0",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "Q1Pad1periphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "299.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "363.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad1periphery1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "Q1Pad1periphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "581.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "581.0um",
                "Y:="			, "-607.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "81.0um",
                "Y:="			, "-607.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "81.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "329.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "329.0um",
                "Y:="			, "-458.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "333.0um",
                "Y:="			, "-458.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "333.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "581.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad2",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oModuleBoundary.AssignThinConductor(
    [
        "NAME:ThinCondQ1Pad2",
        "Objects:="		, ["Q1Pad2"],
        "Material:="		, "perfect conductor",
        "Thickness:="		, "0.1um"
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "581.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "581.0um",
                "Y:="			, "-607.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "81.0um",
                "Y:="			, "-607.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "81.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "329.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "329.0um",
                "Y:="			, "-458.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "333.0um",
                "Y:="			, "-458.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "333.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "581.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad2TrenchComponent",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "681.0um",
                "Y:="			, "-387.00000000000006um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "681.0um",
                "Y:="			, "-709.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-19.0um",
                "Y:="			, "-709.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-19.0um",
                "Y:="			, "-386.99999999999994um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "681.0um",
                "Y:="			, "-387.00000000000006um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad2TrenchPeriphery0",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "363.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "299.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad2TrenchPeriphery1",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q1Pad2TrenchPeriphery0",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "Q1Pad2TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q1Pad2TrenchPeriphery1",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "Q1Pad2TrenchPeriphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q1Pad2",
        "Objects:="		, ["Q1Pad2"]
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "681.0um",
                "Y:="			, "-387.00000000000006um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "681.0um",
                "Y:="			, "-709.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-19.0um",
                "Y:="			, "-709.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-19.0um",
                "Y:="			, "-386.99999999999994um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "681.0um",
                "Y:="			, "-387.00000000000006um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad2periphery0",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "Q1Pad2periphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "363.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "299.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad2periphery1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "Q1Pad2periphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-895.54um",
                "Y:="			, "2406.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-895.54um",
                "Y:="			, "2396.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1090.54um",
                "Y:="			, "2396.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1090.54um",
                "Y:="			, "2371.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1090.54um",
                "Y:="			, "2371.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1090.54um",
                "Y:="			, "2346.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1100.54um",
                "Y:="			, "2346.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1100.54um",
                "Y:="			, "2371.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1100.54um",
                "Y:="			, "2371.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1100.54um",
                "Y:="			, "2396.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1295.54um",
                "Y:="			, "2396.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1295.54um",
                "Y:="			, "2406.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-895.54um",
                "Y:="			, "2406.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 8,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 9,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 10,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 11,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oModuleBoundary.AssignThinConductor(
    [
        "NAME:ThinCondR0Pad1",
        "Objects:="		, ["R0Pad1"],
        "Material:="		, "perfect conductor",
        "Thickness:="		, "0.1um"
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-895.54um",
                "Y:="			, "2406.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-895.54um",
                "Y:="			, "2396.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1090.54um",
                "Y:="			, "2396.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1090.54um",
                "Y:="			, "2371.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1090.54um",
                "Y:="			, "2371.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1090.54um",
                "Y:="			, "2346.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1100.54um",
                "Y:="			, "2346.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1100.54um",
                "Y:="			, "2371.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1100.54um",
                "Y:="			, "2371.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1100.54um",
                "Y:="			, "2396.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1295.54um",
                "Y:="			, "2396.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1295.54um",
                "Y:="			, "2406.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-895.54um",
                "Y:="			, "2406.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 8,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 9,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 10,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 11,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad1TrenchComponent",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-871.54um",
                "Y:="			, "2412.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-871.54um",
                "Y:="			, "2390.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1319.54um",
                "Y:="			, "2390.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1319.54um",
                "Y:="			, "2412.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-871.54um",
                "Y:="			, "2412.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad1TrenchPeriphery0",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2402.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2365.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1106.54um",
                "Y:="			, "2365.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1106.54um",
                "Y:="			, "2402.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2402.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad1TrenchPeriphery1",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2372.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2345.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1106.54um",
                "Y:="			, "2345.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1106.54um",
                "Y:="			, "2372.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2372.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad1TrenchPeriphery2",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R0Pad1TrenchPeriphery0",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R0Pad1TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R0Pad1TrenchPeriphery1",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R0Pad1TrenchPeriphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R0Pad1TrenchPeriphery2",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R0Pad1TrenchPeriphery2"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R0Pad1",
        "Objects:="		, ["R0Pad1"]
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-871.54um",
                "Y:="			, "2412.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-871.54um",
                "Y:="			, "2390.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1319.54um",
                "Y:="			, "2390.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1319.54um",
                "Y:="			, "2412.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-871.54um",
                "Y:="			, "2412.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad1periphery0",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R0Pad1periphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2402.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2365.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1106.54um",
                "Y:="			, "2365.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1106.54um",
                "Y:="			, "2402.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2402.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad1periphery1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R0Pad1periphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2372.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2345.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1106.54um",
                "Y:="			, "2345.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1106.54um",
                "Y:="			, "2372.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2372.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad1periphery2",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R0Pad1periphery2"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-589.0047525137112um",
                "Y:="			, "-400.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.0047525137112um",
                "Y:="			, "-400.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.0047525137112um",
                "Y:="			, "-355.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.0047525137112um",
                "Y:="			, "-355.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.0047525137112um",
                "Y:="			, "-355.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-669.0047525137112um",
                "Y:="			, "-355.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-669.0047525137112um",
                "Y:="			, "-345.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.0047525137112um",
                "Y:="			, "-345.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.0047525137112um",
                "Y:="			, "-345.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.0047525137112um",
                "Y:="			, "-345.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.0047525137112um",
                "Y:="			, "-300.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-589.0047525137112um",
                "Y:="			, "-300.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-589.0047525137112um",
                "Y:="			, "-400.5352474862933um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 8,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 9,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 10,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 11,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad2",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oModuleBoundary.AssignThinConductor(
    [
        "NAME:ThinCondR0Pad2",
        "Objects:="		, ["R0Pad2"],
        "Material:="		, "perfect conductor",
        "Thickness:="		, "0.1um"
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-589.0047525137112um",
                "Y:="			, "-400.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.0047525137112um",
                "Y:="			, "-400.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.0047525137112um",
                "Y:="			, "-355.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.0047525137112um",
                "Y:="			, "-355.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.0047525137112um",
                "Y:="			, "-355.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-669.0047525137112um",
                "Y:="			, "-355.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-669.0047525137112um",
                "Y:="			, "-345.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.0047525137112um",
                "Y:="			, "-345.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.0047525137112um",
                "Y:="			, "-345.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.0047525137112um",
                "Y:="			, "-345.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.0047525137112um",
                "Y:="			, "-300.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-589.0047525137112um",
                "Y:="			, "-300.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-589.0047525137112um",
                "Y:="			, "-400.5352474862933um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 8,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 9,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 10,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 11,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad2TrenchComponent",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-559.0047525137112um",
                "Y:="			, "-430.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-649.0047525137112um",
                "Y:="			, "-430.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-649.0047525137112um",
                "Y:="			, "-270.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-559.0047525137112um",
                "Y:="			, "-270.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-559.0047525137112um",
                "Y:="			, "-430.5352474862933um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad2TrenchPeriphery0",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-613.0047525137112um",
                "Y:="			, "-361.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-650.0047525137112um",
                "Y:="			, "-361.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-650.0047525137112um",
                "Y:="			, "-339.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-613.0047525137112um",
                "Y:="			, "-339.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-613.0047525137112um",
                "Y:="			, "-361.5352474862933um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad2TrenchPeriphery1",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-643.0047525137112um",
                "Y:="			, "-361.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-670.0047525137112um",
                "Y:="			, "-361.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-670.0047525137112um",
                "Y:="			, "-339.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-643.0047525137112um",
                "Y:="			, "-339.5352474862933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-643.0047525137112um",
                "Y:="			, "-361.5352474862933um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad2TrenchPeriphery2",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R0Pad2TrenchPeriphery0",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R0Pad2TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R0Pad2TrenchPeriphery1",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R0Pad2TrenchPeriphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R0Pad2TrenchPeriphery2",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R0Pad2TrenchPeriphery2"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R0Pad2",
        "Objects:="		, ["R0Pad2"]
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-559.0047525137112um",
                "Y:="			, "-430.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-649.0047525137112um",
                "Y:="			, "-430.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-649.0047525137112um",
                "Y:="			, "-270.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-559.0047525137112um",
                "Y:="			, "-270.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-559.0047525137112um",
                "Y:="			, "-430.5352474862933um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad2periphery0",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R0Pad2periphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-613.0047525137112um",
                "Y:="			, "-361.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-650.0047525137112um",
                "Y:="			, "-361.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-650.0047525137112um",
                "Y:="			, "-339.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-613.0047525137112um",
                "Y:="			, "-339.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-613.0047525137112um",
                "Y:="			, "-361.5352474862933um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad2periphery1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R0Pad2periphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-643.0047525137112um",
                "Y:="			, "-361.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-670.0047525137112um",
                "Y:="			, "-361.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-670.0047525137112um",
                "Y:="			, "-339.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-643.0047525137112um",
                "Y:="			, "-339.5352474862933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-643.0047525137112um",
                "Y:="			, "-361.5352474862933um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad2periphery2",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R0Pad2periphery2"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "1316.0um",
                "Y:="			, "2406.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1316.0um",
                "Y:="			, "2396.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1121.0um",
                "Y:="			, "2396.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1121.0um",
                "Y:="			, "2371.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1121.0um",
                "Y:="			, "2371.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1121.0um",
                "Y:="			, "2346.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1111.0um",
                "Y:="			, "2346.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1111.0um",
                "Y:="			, "2371.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1111.0um",
                "Y:="			, "2371.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1111.0um",
                "Y:="			, "2396.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "916.0um",
                "Y:="			, "2396.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "916.0um",
                "Y:="			, "2406.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1316.0um",
                "Y:="			, "2406.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 8,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 9,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 10,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 11,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oModuleBoundary.AssignThinConductor(
    [
        "NAME:ThinCondR1Pad1",
        "Objects:="		, ["R1Pad1"],
        "Material:="		, "perfect conductor",
        "Thickness:="		, "0.1um"
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "1316.0um",
                "Y:="			, "2406.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1316.0um",
                "Y:="			, "2396.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1121.0um",
                "Y:="			, "2396.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1121.0um",
                "Y:="			, "2371.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1121.0um",
                "Y:="			, "2371.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1121.0um",
                "Y:="			, "2346.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1111.0um",
                "Y:="			, "2346.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1111.0um",
                "Y:="			, "2371.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1111.0um",
                "Y:="			, "2371.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1111.0um",
                "Y:="			, "2396.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "916.0um",
                "Y:="			, "2396.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "916.0um",
                "Y:="			, "2406.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1316.0um",
                "Y:="			, "2406.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 8,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 9,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 10,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 11,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad1TrenchComponent",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "1340.0um",
                "Y:="			, "2412.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1340.0um",
                "Y:="			, "2390.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "892.0um",
                "Y:="			, "2390.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "892.0um",
                "Y:="			, "2412.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1340.0um",
                "Y:="			, "2412.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad1TrenchPeriphery0",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2402.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2365.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1105.0um",
                "Y:="			, "2365.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1105.0um",
                "Y:="			, "2402.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2402.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad1TrenchPeriphery1",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2372.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2345.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1105.0um",
                "Y:="			, "2345.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1105.0um",
                "Y:="			, "2372.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2372.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad1TrenchPeriphery2",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R1Pad1TrenchPeriphery0",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R1Pad1TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R1Pad1TrenchPeriphery1",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R1Pad1TrenchPeriphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R1Pad1TrenchPeriphery2",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R1Pad1TrenchPeriphery2"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R1Pad1",
        "Objects:="		, ["R1Pad1"]
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "1340.0um",
                "Y:="			, "2412.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1340.0um",
                "Y:="			, "2390.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "892.0um",
                "Y:="			, "2390.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "892.0um",
                "Y:="			, "2412.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1340.0um",
                "Y:="			, "2412.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad1periphery0",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R1Pad1periphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2402.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2365.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1105.0um",
                "Y:="			, "2365.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1105.0um",
                "Y:="			, "2402.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2402.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad1periphery1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R1Pad1periphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2372.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2345.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1105.0um",
                "Y:="			, "2345.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1105.0um",
                "Y:="			, "2372.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2372.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad1periphery2",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R1Pad1periphery2"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "609.1464426275538um",
                "Y:="			, "-301.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.1464426275538um",
                "Y:="			, "-301.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.1464426275538um",
                "Y:="			, "-346.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.1464426275538um",
                "Y:="			, "-346.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.1464426275538um",
                "Y:="			, "-346.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "689.1464426275538um",
                "Y:="			, "-346.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "689.1464426275538um",
                "Y:="			, "-356.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.1464426275538um",
                "Y:="			, "-356.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.1464426275538um",
                "Y:="			, "-356.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.1464426275538um",
                "Y:="			, "-356.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.1464426275538um",
                "Y:="			, "-401.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "609.1464426275538um",
                "Y:="			, "-401.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "609.1464426275538um",
                "Y:="			, "-301.353557372477um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 8,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 9,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 10,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 11,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad2",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oModuleBoundary.AssignThinConductor(
    [
        "NAME:ThinCondR1Pad2",
        "Objects:="		, ["R1Pad2"],
        "Material:="		, "perfect conductor",
        "Thickness:="		, "0.1um"
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "609.1464426275538um",
                "Y:="			, "-301.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.1464426275538um",
                "Y:="			, "-301.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.1464426275538um",
                "Y:="			, "-346.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.1464426275538um",
                "Y:="			, "-346.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.1464426275538um",
                "Y:="			, "-346.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "689.1464426275538um",
                "Y:="			, "-346.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "689.1464426275538um",
                "Y:="			, "-356.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.1464426275538um",
                "Y:="			, "-356.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.1464426275538um",
                "Y:="			, "-356.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.1464426275538um",
                "Y:="			, "-356.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.1464426275538um",
                "Y:="			, "-401.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "609.1464426275538um",
                "Y:="			, "-401.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "609.1464426275538um",
                "Y:="			, "-301.353557372477um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 8,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 9,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 10,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 11,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad2TrenchComponent",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "579.1464426275538um",
                "Y:="			, "-271.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "669.1464426275538um",
                "Y:="			, "-271.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "669.1464426275538um",
                "Y:="			, "-431.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "579.1464426275538um",
                "Y:="			, "-431.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "579.1464426275538um",
                "Y:="			, "-271.353557372477um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad2TrenchPeriphery0",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "633.1464426275538um",
                "Y:="			, "-340.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "670.1464426275538um",
                "Y:="			, "-340.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "670.1464426275538um",
                "Y:="			, "-362.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "633.1464426275538um",
                "Y:="			, "-362.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "633.1464426275538um",
                "Y:="			, "-340.353557372477um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad2TrenchPeriphery1",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "663.1464426275538um",
                "Y:="			, "-340.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "690.1464426275538um",
                "Y:="			, "-340.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "690.1464426275538um",
                "Y:="			, "-362.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "663.1464426275538um",
                "Y:="			, "-362.353557372477um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "663.1464426275538um",
                "Y:="			, "-340.353557372477um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad2TrenchPeriphery2",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R1Pad2TrenchPeriphery0",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R1Pad2TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R1Pad2TrenchPeriphery1",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R1Pad2TrenchPeriphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R1Pad2TrenchPeriphery2",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R1Pad2TrenchPeriphery2"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R1Pad2",
        "Objects:="		, ["R1Pad2"]
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "579.1464426275538um",
                "Y:="			, "-271.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "669.1464426275538um",
                "Y:="			, "-271.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "669.1464426275538um",
                "Y:="			, "-431.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "579.1464426275538um",
                "Y:="			, "-431.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "579.1464426275538um",
                "Y:="			, "-271.353557372477um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad2periphery0",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R1Pad2periphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "633.1464426275538um",
                "Y:="			, "-340.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "670.1464426275538um",
                "Y:="			, "-340.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "670.1464426275538um",
                "Y:="			, "-362.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "633.1464426275538um",
                "Y:="			, "-362.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "633.1464426275538um",
                "Y:="			, "-340.353557372477um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad2periphery1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R1Pad2periphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "663.1464426275538um",
                "Y:="			, "-340.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "690.1464426275538um",
                "Y:="			, "-340.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "690.1464426275538um",
                "Y:="			, "-362.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "663.1464426275538um",
                "Y:="			, "-362.353557372477um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "663.1464426275538um",
                "Y:="			, "-340.353557372477um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad2periphery2",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R1Pad2periphery2"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q0Pad1TrenchComponent",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Unite(
    [
        "NAME:Selections",
        "Selections:="		, "S0,Q0Pad1TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q0Pad2TrenchComponent",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Unite(
    [
        "NAME:Selections",
        "Selections:="		, "S0,Q0Pad2TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q1Pad1TrenchComponent",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Unite(
    [
        "NAME:Selections",
        "Selections:="		, "S0,Q1Pad1TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q1Pad2TrenchComponent",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Unite(
    [
        "NAME:Selections",
        "Selections:="		, "S0,Q1Pad2TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R0Pad1TrenchComponent",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Unite(
    [
        "NAME:Selections",
        "Selections:="		, "S0,R0Pad1TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R0Pad2TrenchComponent",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Unite(
    [
        "NAME:Selections",
        "Selections:="		, "S0,R0Pad2TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R1Pad1TrenchComponent",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Unite(
    [
        "NAME:Selections",
        "Selections:="		, "S0,R1Pad1TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R1Pad2TrenchComponent",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Unite(
    [
        "NAME:Selections",
        "Selections:="		, "S0,R1Pad2TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oModuleBoundary.AssignThinConductor(
    [
        "NAME:ThinCondG0",
        "Objects:="		, ["G0"],
        "Material:="		, "perfect conductor",
        "Thickness:="		, "0.1um"
    ])
oModuleBoundary.AssignGroundNet(
    [
        "NAME:GroundNet1",
        "Objects:="		, ["G0"]
    ])
oModuleAnalysis = oDesign.GetModule("AnalysisSetup")
oModuleAnalysis.InsertSetup("Matrix",
    [
        "NAME:capSim",
        "AdaptiveFreq:="	, "5GHz",
        "SaveFields:="		, False,
        "Enabled:="		, True,
        [
            "NAME:Cap",
            "MaxPass:="		, 99,
            "MinPass:="		, 1,
            "MinConvPass:="		, 1,
            "PerError:="		, 1,
            "PerRefine:="		, 100,
            "AutoIncreaseSolutionOrder:=", True,
            "SolutionOrder:="	, "High",
            "Solver Type:="		, "Iterative"
        ]
    ])
oDesign.AnalyzeAll()
oDesign.ExportMatrixData("/beegfs/scratch/joelhoward/QSMSimulations/QSMTests/SWIFT500um/capMat/q3dExtractor_Results.csv", "C", "", "capSim:LastAdaptive", "Original", "ohm", "nH", "pF", "mSie", 1000000000, "Maxwell,Spice,Couple", 0, False, 5, 8, 0)
oProject.Save()
