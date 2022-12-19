import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("capMatExtractor")
oProject.InsertDesign("Q3D Extractor", "capMatExtractor", "", "")
oDesign = oProject.SetActiveDesign("capMatExtractor")
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
                "X:="			, "-7000.0um",
                "Y:="			, "-8000.0um",
                "Z:="			, "0um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-7000.0um",
                "Y:="			, "8000.0um",
                "Z:="			, "0um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "7000.0um",
                "Y:="			, "8000.0um",
                "Z:="			, "0um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "7000.0um",
                "Y:="			, "-8000.0um",
                "Z:="			, "0um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-7000.0um",
                "Y:="			, "-8000.0um",
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
                "X:="			, "-7000.0um",
                "Y:="			, "-8000.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-7000.0um",
                "Y:="			, "8000.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "7000.0um",
                "Y:="			, "8000.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "7000.0um",
                "Y:="			, "-8000.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-7000.0um",
                "Y:="			, "-8000.0um",
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
                "X:="			, "-2450.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2450.0um",
                "Y:="			, "2155.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1950.0um",
                "Y:="			, "2155.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1950.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2198.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2198.0um",
                "Y:="			, "2004.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2202.0um",
                "Y:="			, "2004.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2202.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2450.0um",
                "Y:="			, "2015.0um",
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
                "X:="			, "-2450.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2450.0um",
                "Y:="			, "2155.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1950.0um",
                "Y:="			, "2155.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1950.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2198.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2198.0um",
                "Y:="			, "2004.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2202.0um",
                "Y:="			, "2004.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2202.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2450.0um",
                "Y:="			, "2015.0um",
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
                "X:="			, "-2550.0um",
                "Y:="			, "1915.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2550.0um",
                "Y:="			, "2255.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1850.0um",
                "Y:="			, "2255.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1850.0um",
                "Y:="			, "1915.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2550.0um",
                "Y:="			, "1915.0um",
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
                "X:="			, "-2202.0um",
                "Y:="			, "2004.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2202.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2198.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2198.0um",
                "Y:="			, "2004.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2202.0um",
                "Y:="			, "2004.0um",
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
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-2550.0um",
                "Y:="			, "1915.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2550.0um",
                "Y:="			, "2255.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1850.0um",
                "Y:="			, "2255.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1850.0um",
                "Y:="			, "1915.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2550.0um",
                "Y:="			, "1915.0um",
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
                "X:="			, "-2202.0um",
                "Y:="			, "2004.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2202.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2198.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2198.0um",
                "Y:="			, "2004.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2202.0um",
                "Y:="			, "2004.0um",
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
                "X:="			, "-1950.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1950.0um",
                "Y:="			, "1845.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2450.0um",
                "Y:="			, "1845.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2450.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2202.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2202.0um",
                "Y:="			, "1996.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2198.0um",
                "Y:="			, "1996.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2198.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1950.0um",
                "Y:="			, "1985.0um",
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
                "X:="			, "-1950.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1950.0um",
                "Y:="			, "1845.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2450.0um",
                "Y:="			, "1845.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2450.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2202.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2202.0um",
                "Y:="			, "1996.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2198.0um",
                "Y:="			, "1996.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2198.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1950.0um",
                "Y:="			, "1985.0um",
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
                "X:="			, "-1850.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1850.0um",
                "Y:="			, "1745.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2550.0um",
                "Y:="			, "1745.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2550.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1850.0um",
                "Y:="			, "2085.0um",
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
                "X:="			, "-2198.0um",
                "Y:="			, "1996.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2198.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2202.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2202.0um",
                "Y:="			, "1996.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2198.0um",
                "Y:="			, "1996.0um",
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
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-1850.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1850.0um",
                "Y:="			, "1745.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2550.0um",
                "Y:="			, "1745.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2550.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1850.0um",
                "Y:="			, "2085.0um",
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
                "X:="			, "-2198.0um",
                "Y:="			, "1996.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2198.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2202.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2202.0um",
                "Y:="			, "1996.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2198.0um",
                "Y:="			, "1996.0um",
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
                "X:="			, "-1650.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1650.0um",
                "Y:="			, "2155.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1150.0um",
                "Y:="			, "2155.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1150.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1398.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1398.0um",
                "Y:="			, "2004.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1402.0um",
                "Y:="			, "2004.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1402.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1650.0um",
                "Y:="			, "2015.0um",
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
                "X:="			, "-1650.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1650.0um",
                "Y:="			, "2155.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1150.0um",
                "Y:="			, "2155.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1150.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1398.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1398.0um",
                "Y:="			, "2004.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1402.0um",
                "Y:="			, "2004.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1402.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1650.0um",
                "Y:="			, "2015.0um",
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
                "X:="			, "-1750.0um",
                "Y:="			, "1915.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1750.0um",
                "Y:="			, "2255.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1050.0um",
                "Y:="			, "2255.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1050.0um",
                "Y:="			, "1915.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1750.0um",
                "Y:="			, "1915.0um",
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
                "X:="			, "-1402.0um",
                "Y:="			, "2004.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1402.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1398.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1398.0um",
                "Y:="			, "2004.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1402.0um",
                "Y:="			, "2004.0um",
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
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-1750.0um",
                "Y:="			, "1915.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1750.0um",
                "Y:="			, "2255.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1050.0um",
                "Y:="			, "2255.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1050.0um",
                "Y:="			, "1915.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1750.0um",
                "Y:="			, "1915.0um",
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
                "X:="			, "-1402.0um",
                "Y:="			, "2004.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1402.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1398.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1398.0um",
                "Y:="			, "2004.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1402.0um",
                "Y:="			, "2004.0um",
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
                "X:="			, "-1150.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1150.0um",
                "Y:="			, "1845.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1650.0um",
                "Y:="			, "1845.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1650.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1402.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1402.0um",
                "Y:="			, "1996.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1398.0um",
                "Y:="			, "1996.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1398.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1150.0um",
                "Y:="			, "1985.0um",
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
                "X:="			, "-1150.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1150.0um",
                "Y:="			, "1845.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1650.0um",
                "Y:="			, "1845.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1650.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1402.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1402.0um",
                "Y:="			, "1996.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1398.0um",
                "Y:="			, "1996.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1398.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1150.0um",
                "Y:="			, "1985.0um",
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
                "X:="			, "-1050.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1050.0um",
                "Y:="			, "1745.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1750.0um",
                "Y:="			, "1745.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1750.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1050.0um",
                "Y:="			, "2085.0um",
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
                "X:="			, "-1398.0um",
                "Y:="			, "1996.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1398.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1402.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1402.0um",
                "Y:="			, "1996.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1398.0um",
                "Y:="			, "1996.0um",
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
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-1050.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1050.0um",
                "Y:="			, "1745.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1750.0um",
                "Y:="			, "1745.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1750.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1050.0um",
                "Y:="			, "2085.0um",
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
                "X:="			, "-1398.0um",
                "Y:="			, "1996.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1398.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1402.0um",
                "Y:="			, "1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1402.0um",
                "Y:="			, "1996.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1398.0um",
                "Y:="			, "1996.0um",
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
                "X:="			, "150.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "150.0um",
                "Y:="			, "2255.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "650.0um",
                "Y:="			, "2255.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "650.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "402.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "402.0um",
                "Y:="			, "2104.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "398.0um",
                "Y:="			, "2104.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "398.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "150.0um",
                "Y:="			, "2115.0um",
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
        "Name:="		, "Q2Pad1",
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
        "NAME:ThinCondQ2Pad1",
        "Objects:="		, ["Q2Pad1"],
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
                "X:="			, "150.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "150.0um",
                "Y:="			, "2255.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "650.0um",
                "Y:="			, "2255.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "650.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "402.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "402.0um",
                "Y:="			, "2104.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "398.0um",
                "Y:="			, "2104.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "398.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "150.0um",
                "Y:="			, "2115.0um",
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
        "Name:="		, "Q2Pad1TrenchComponent",
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
                "X:="			, "50.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "50.0um",
                "Y:="			, "2355.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "750.0um",
                "Y:="			, "2355.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "750.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "50.0um",
                "Y:="			, "2015.0um",
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
        "Name:="		, "Q2Pad1TrenchPeriphery0",
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
                "X:="			, "398.0um",
                "Y:="			, "2104.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "398.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "402.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "402.0um",
                "Y:="			, "2104.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "398.0um",
                "Y:="			, "2104.0um",
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
        "Name:="		, "Q2Pad1TrenchPeriphery1",
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
        "Selections:="		, "Q2Pad1TrenchPeriphery0",
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
        "Tool Parts:="		, "Q2Pad1TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q2Pad1TrenchPeriphery1",
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
        "Tool Parts:="		, "Q2Pad1TrenchPeriphery1"
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
                "X:="			, "50.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "50.0um",
                "Y:="			, "2355.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "750.0um",
                "Y:="			, "2355.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "750.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "50.0um",
                "Y:="			, "2015.0um",
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
        "Name:="		, "Q2Pad1periphery0",
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
        "Tool Parts:="		, "Q2Pad1periphery0"
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
                "X:="			, "398.0um",
                "Y:="			, "2104.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "398.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "402.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "402.0um",
                "Y:="			, "2104.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "398.0um",
                "Y:="			, "2104.0um",
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
        "Name:="		, "Q2Pad1periphery1",
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
        "Tool Parts:="		, "Q2Pad1periphery1"
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
                "X:="			, "650.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "650.0um",
                "Y:="			, "1945.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "150.0um",
                "Y:="			, "1945.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "150.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "398.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "398.0um",
                "Y:="			, "2096.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "402.0um",
                "Y:="			, "2096.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "402.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "650.0um",
                "Y:="			, "2085.0um",
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
        "Name:="		, "Q2Pad2",
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
        "NAME:ThinCondQ2Pad2",
        "Objects:="		, ["Q2Pad2"],
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
                "X:="			, "650.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "650.0um",
                "Y:="			, "1945.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "150.0um",
                "Y:="			, "1945.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "150.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "398.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "398.0um",
                "Y:="			, "2096.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "402.0um",
                "Y:="			, "2096.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "402.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "650.0um",
                "Y:="			, "2085.0um",
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
        "Name:="		, "Q2Pad2TrenchComponent",
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
                "X:="			, "750.0um",
                "Y:="			, "2185.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "750.0um",
                "Y:="			, "1845.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "50.0um",
                "Y:="			, "1845.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "50.0um",
                "Y:="			, "2185.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "750.0um",
                "Y:="			, "2185.0um",
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
        "Name:="		, "Q2Pad2TrenchPeriphery0",
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
                "X:="			, "402.0um",
                "Y:="			, "2096.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "402.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "398.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "398.0um",
                "Y:="			, "2096.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "402.0um",
                "Y:="			, "2096.0um",
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
        "Name:="		, "Q2Pad2TrenchPeriphery1",
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
        "Selections:="		, "Q2Pad2TrenchPeriphery0",
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
        "Tool Parts:="		, "Q2Pad2TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q2Pad2TrenchPeriphery1",
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
        "Tool Parts:="		, "Q2Pad2TrenchPeriphery1"
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
                "X:="			, "750.0um",
                "Y:="			, "2185.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "750.0um",
                "Y:="			, "1845.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "50.0um",
                "Y:="			, "1845.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "50.0um",
                "Y:="			, "2185.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "750.0um",
                "Y:="			, "2185.0um",
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
        "Name:="		, "Q2Pad2periphery0",
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
        "Tool Parts:="		, "Q2Pad2periphery0"
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
                "X:="			, "402.0um",
                "Y:="			, "2096.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "402.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "398.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "398.0um",
                "Y:="			, "2096.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "402.0um",
                "Y:="			, "2096.0um",
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
        "Name:="		, "Q2Pad2periphery1",
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
        "Tool Parts:="		, "Q2Pad2periphery1"
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
                "X:="			, "950.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "950.0um",
                "Y:="			, "2255.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1450.0um",
                "Y:="			, "2255.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1450.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "2104.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "2104.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "950.0um",
                "Y:="			, "2115.0um",
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
        "Name:="		, "Q3Pad1",
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
        "NAME:ThinCondQ3Pad1",
        "Objects:="		, ["Q3Pad1"],
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
                "X:="			, "950.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "950.0um",
                "Y:="			, "2255.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1450.0um",
                "Y:="			, "2255.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1450.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "2104.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "2104.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "950.0um",
                "Y:="			, "2115.0um",
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
        "Name:="		, "Q3Pad1TrenchComponent",
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
                "X:="			, "850.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "850.0um",
                "Y:="			, "2355.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1550.0um",
                "Y:="			, "2355.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1550.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "850.0um",
                "Y:="			, "2015.0um",
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
        "Name:="		, "Q3Pad1TrenchPeriphery0",
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
                "X:="			, "1198.0um",
                "Y:="			, "2104.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "2104.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "2104.0um",
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
        "Name:="		, "Q3Pad1TrenchPeriphery1",
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
        "Selections:="		, "Q3Pad1TrenchPeriphery0",
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
        "Tool Parts:="		, "Q3Pad1TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q3Pad1TrenchPeriphery1",
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
        "Tool Parts:="		, "Q3Pad1TrenchPeriphery1"
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
                "X:="			, "850.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "850.0um",
                "Y:="			, "2355.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1550.0um",
                "Y:="			, "2355.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1550.0um",
                "Y:="			, "2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "850.0um",
                "Y:="			, "2015.0um",
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
        "Name:="		, "Q3Pad1periphery0",
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
        "Tool Parts:="		, "Q3Pad1periphery0"
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
                "X:="			, "1198.0um",
                "Y:="			, "2104.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "2115.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "2104.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "2104.0um",
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
        "Name:="		, "Q3Pad1periphery1",
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
        "Tool Parts:="		, "Q3Pad1periphery1"
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
                "X:="			, "1450.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1450.0um",
                "Y:="			, "1945.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "950.0um",
                "Y:="			, "1945.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "950.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "2096.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "2096.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1450.0um",
                "Y:="			, "2085.0um",
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
        "Name:="		, "Q3Pad2",
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
        "NAME:ThinCondQ3Pad2",
        "Objects:="		, ["Q3Pad2"],
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
                "X:="			, "1450.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1450.0um",
                "Y:="			, "1945.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "950.0um",
                "Y:="			, "1945.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "950.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "2096.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "2096.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1450.0um",
                "Y:="			, "2085.0um",
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
        "Name:="		, "Q3Pad2TrenchComponent",
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
                "X:="			, "1550.0um",
                "Y:="			, "2185.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1550.0um",
                "Y:="			, "1845.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "850.0um",
                "Y:="			, "1845.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "850.0um",
                "Y:="			, "2185.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1550.0um",
                "Y:="			, "2185.0um",
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
        "Name:="		, "Q3Pad2TrenchPeriphery0",
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
                "X:="			, "1202.0um",
                "Y:="			, "2096.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "2096.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "2096.0um",
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
        "Name:="		, "Q3Pad2TrenchPeriphery1",
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
        "Selections:="		, "Q3Pad2TrenchPeriphery0",
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
        "Tool Parts:="		, "Q3Pad2TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q3Pad2TrenchPeriphery1",
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
        "Tool Parts:="		, "Q3Pad2TrenchPeriphery1"
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
                "X:="			, "1550.0um",
                "Y:="			, "2185.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1550.0um",
                "Y:="			, "1845.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "850.0um",
                "Y:="			, "1845.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "850.0um",
                "Y:="			, "2185.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1550.0um",
                "Y:="			, "2185.0um",
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
        "Name:="		, "Q3Pad2periphery0",
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
        "Tool Parts:="		, "Q3Pad2periphery0"
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
                "X:="			, "1202.0um",
                "Y:="			, "2096.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "2085.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "2096.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "2096.0um",
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
        "Name:="		, "Q3Pad2periphery1",
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
        "Tool Parts:="		, "Q3Pad2periphery1"
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
                "X:="			, "1184.800923078339um",
                "Y:="			, "350.0120241677024um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1044.8009674678824um",
                "Y:="			, "350.12350990720506um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1045.199130823249um",
                "Y:="			, "850.1233513731223um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1185.1990864337058um",
                "Y:="			, "850.0118656336197um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1185.001597409444um",
                "Y:="			, "602.0119442665247um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1196.0015939216942um",
                "Y:="			, "602.0031846727067um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1195.9984086148513um",
                "Y:="			, "598.0031859409793um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1184.9984121026012um",
                "Y:="			, "598.0119455347974um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1184.800923078339um",
                "Y:="			, "350.0120241677024um",
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
        "Name:="		, "Q4Pad1",
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
        "NAME:ThinCondQ4Pad1",
        "Objects:="		, ["Q4Pad1"],
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
                "X:="			, "1184.800923078339um",
                "Y:="			, "350.0120241677024um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1044.8009674678824um",
                "Y:="			, "350.12350990720506um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1045.199130823249um",
                "Y:="			, "850.1233513731223um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1185.1990864337058um",
                "Y:="			, "850.0118656336197um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1185.001597409444um",
                "Y:="			, "602.0119442665247um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1196.0015939216942um",
                "Y:="			, "602.0031846727067um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1195.9984086148513um",
                "Y:="			, "598.0031859409793um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1184.9984121026012um",
                "Y:="			, "598.0119455347974um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1184.800923078339um",
                "Y:="			, "350.0120241677024um",
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
        "Name:="		, "Q4Pad1TrenchComponent",
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
                "X:="			, "1284.7212587004494um",
                "Y:="			, "249.93242320344558um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "944.7213665036256um",
                "Y:="			, "250.20317428509492um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "945.2787952011388um",
                "Y:="			, "950.2029523373792um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1285.2786873979626um",
                "Y:="			, "949.9322012557298um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1284.7212587004494um",
                "Y:="			, "249.93242320344558um",
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
        "Name:="		, "Q4Pad1TrenchPeriphery0",
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
                "X:="			, "1195.9984086148513um",
                "Y:="			, "598.0031859409793um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1184.9984121026012um",
                "Y:="			, "598.0119455347974um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1185.001597409444um",
                "Y:="			, "602.0119442665247um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1196.0015939216942um",
                "Y:="			, "602.0031846727067um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1195.9984086148513um",
                "Y:="			, "598.0031859409793um",
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
        "Name:="		, "Q4Pad1TrenchPeriphery1",
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
        "Selections:="		, "Q4Pad1TrenchPeriphery0",
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
        "Tool Parts:="		, "Q4Pad1TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q4Pad1TrenchPeriphery1",
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
        "Tool Parts:="		, "Q4Pad1TrenchPeriphery1"
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
                "X:="			, "1284.7212587004494um",
                "Y:="			, "249.93242320344558um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "944.7213665036256um",
                "Y:="			, "250.20317428509492um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "945.2787952011388um",
                "Y:="			, "950.2029523373792um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1285.2786873979626um",
                "Y:="			, "949.9322012557298um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1284.7212587004494um",
                "Y:="			, "249.93242320344558um",
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
        "Name:="		, "Q4Pad1periphery0",
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
        "Tool Parts:="		, "Q4Pad1periphery0"
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
                "X:="			, "1195.9984086148513um",
                "Y:="			, "598.0031859409793um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1184.9984121026012um",
                "Y:="			, "598.0119455347974um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1185.001597409444um",
                "Y:="			, "602.0119442665247um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1196.0015939216942um",
                "Y:="			, "602.0031846727067um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1195.9984086148513um",
                "Y:="			, "598.0031859409793um",
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
        "Name:="		, "Q4Pad1periphery1",
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
        "Tool Parts:="		, "Q4Pad1periphery1"
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
                "X:="			, "1215.1990769216607um",
                "Y:="			, "849.9879758322976um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1355.1990325321176um",
                "Y:="			, "849.8764900927949um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1354.8008691767511um",
                "Y:="			, "349.8766486268777um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1214.8009135662942um",
                "Y:="			, "349.98813436638034um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1214.998402590556um",
                "Y:="			, "597.9880557334753um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1203.9984060783058um",
                "Y:="			, "597.9968153272933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1204.0015913851487um",
                "Y:="			, "601.9968140590207um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1215.0015878973988um",
                "Y:="			, "601.9880544652026um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1215.1990769216607um",
                "Y:="			, "849.9879758322976um",
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
        "Name:="		, "Q4Pad2",
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
        "NAME:ThinCondQ4Pad2",
        "Objects:="		, ["Q4Pad2"],
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
                "X:="			, "1215.1990769216607um",
                "Y:="			, "849.9879758322976um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1355.1990325321176um",
                "Y:="			, "849.8764900927949um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1354.8008691767511um",
                "Y:="			, "349.8766486268777um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1214.8009135662942um",
                "Y:="			, "349.98813436638034um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1214.998402590556um",
                "Y:="			, "597.9880557334753um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1203.9984060783058um",
                "Y:="			, "597.9968153272933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1204.0015913851487um",
                "Y:="			, "601.9968140590207um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1215.0015878973988um",
                "Y:="			, "601.9880544652026um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1215.1990769216607um",
                "Y:="			, "849.9879758322976um",
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
        "Name:="		, "Q4Pad2TrenchComponent",
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
                "X:="			, "1115.2787412995506um",
                "Y:="			, "950.0675767965544um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1455.2786334963744um",
                "Y:="			, "949.7968257149051um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1454.7212047988612um",
                "Y:="			, "249.7970476626209um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1114.7213126020374um",
                "Y:="			, "250.06779874427014um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1115.2787412995506um",
                "Y:="			, "950.0675767965544um",
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
        "Name:="		, "Q4Pad2TrenchPeriphery0",
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
                "X:="			, "1204.0015913851487um",
                "Y:="			, "601.9968140590207um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1215.0015878973988um",
                "Y:="			, "601.9880544652026um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1214.998402590556um",
                "Y:="			, "597.9880557334753um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1203.9984060783058um",
                "Y:="			, "597.9968153272933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1204.0015913851487um",
                "Y:="			, "601.9968140590207um",
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
        "Name:="		, "Q4Pad2TrenchPeriphery1",
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
        "Selections:="		, "Q4Pad2TrenchPeriphery0",
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
        "Tool Parts:="		, "Q4Pad2TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q4Pad2TrenchPeriphery1",
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
        "Tool Parts:="		, "Q4Pad2TrenchPeriphery1"
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
                "X:="			, "1115.2787412995506um",
                "Y:="			, "950.0675767965544um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1455.2786334963744um",
                "Y:="			, "949.7968257149051um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1454.7212047988612um",
                "Y:="			, "249.7970476626209um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1114.7213126020374um",
                "Y:="			, "250.06779874427014um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1115.2787412995506um",
                "Y:="			, "950.0675767965544um",
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
        "Name:="		, "Q4Pad2periphery0",
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
        "Tool Parts:="		, "Q4Pad2periphery0"
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
                "X:="			, "1204.0015913851487um",
                "Y:="			, "601.9968140590207um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1215.0015878973988um",
                "Y:="			, "601.9880544652026um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1214.998402590556um",
                "Y:="			, "597.9880557334753um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1203.9984060783058um",
                "Y:="			, "597.9968153272933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1204.0015913851487um",
                "Y:="			, "601.9968140590207um",
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
        "Name:="		, "Q4Pad2periphery1",
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
        "Tool Parts:="		, "Q4Pad2periphery1"
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
                "X:="			, "1184.800923078339um",
                "Y:="			, "-849.9879758322976um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1044.8009674678824um",
                "Y:="			, "-849.8764900927949um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1045.199130823249um",
                "Y:="			, "-349.8766486268777um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1185.1990864337058um",
                "Y:="			, "-349.98813436638034um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1185.001597409444um",
                "Y:="			, "-597.9880557334753um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1196.0015939216942um",
                "Y:="			, "-597.9968153272933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1195.9984086148513um",
                "Y:="			, "-601.9968140590207um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1184.9984121026012um",
                "Y:="			, "-601.9880544652026um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1184.800923078339um",
                "Y:="			, "-849.9879758322976um",
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
        "Name:="		, "Q5Pad1",
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
        "NAME:ThinCondQ5Pad1",
        "Objects:="		, ["Q5Pad1"],
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
                "X:="			, "1184.800923078339um",
                "Y:="			, "-849.9879758322976um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1044.8009674678824um",
                "Y:="			, "-849.8764900927949um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1045.199130823249um",
                "Y:="			, "-349.8766486268777um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1185.1990864337058um",
                "Y:="			, "-349.98813436638034um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1185.001597409444um",
                "Y:="			, "-597.9880557334753um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1196.0015939216942um",
                "Y:="			, "-597.9968153272933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1195.9984086148513um",
                "Y:="			, "-601.9968140590207um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1184.9984121026012um",
                "Y:="			, "-601.9880544652026um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1184.800923078339um",
                "Y:="			, "-849.9879758322976um",
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
        "Name:="		, "Q5Pad1TrenchComponent",
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
                "X:="			, "1284.7212587004494um",
                "Y:="			, "-950.0675767965545um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "944.7213665036256um",
                "Y:="			, "-949.796825714905um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "945.2787952011388um",
                "Y:="			, "-249.79704766262086um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1285.2786873979626um",
                "Y:="			, "-250.0677987442702um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1284.7212587004494um",
                "Y:="			, "-950.0675767965545um",
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
        "Name:="		, "Q5Pad1TrenchPeriphery0",
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
                "X:="			, "1195.9984086148513um",
                "Y:="			, "-601.9968140590207um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1184.9984121026012um",
                "Y:="			, "-601.9880544652026um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1185.001597409444um",
                "Y:="			, "-597.9880557334753um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1196.0015939216942um",
                "Y:="			, "-597.9968153272933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1195.9984086148513um",
                "Y:="			, "-601.9968140590207um",
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
        "Name:="		, "Q5Pad1TrenchPeriphery1",
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
        "Selections:="		, "Q5Pad1TrenchPeriphery0",
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
        "Tool Parts:="		, "Q5Pad1TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q5Pad1TrenchPeriphery1",
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
        "Tool Parts:="		, "Q5Pad1TrenchPeriphery1"
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
                "X:="			, "1284.7212587004494um",
                "Y:="			, "-950.0675767965545um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "944.7213665036256um",
                "Y:="			, "-949.796825714905um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "945.2787952011388um",
                "Y:="			, "-249.79704766262086um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1285.2786873979626um",
                "Y:="			, "-250.0677987442702um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1284.7212587004494um",
                "Y:="			, "-950.0675767965545um",
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
        "Name:="		, "Q5Pad1periphery0",
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
        "Tool Parts:="		, "Q5Pad1periphery0"
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
                "X:="			, "1195.9984086148513um",
                "Y:="			, "-601.9968140590207um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1184.9984121026012um",
                "Y:="			, "-601.9880544652026um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1185.001597409444um",
                "Y:="			, "-597.9880557334753um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1196.0015939216942um",
                "Y:="			, "-597.9968153272933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1195.9984086148513um",
                "Y:="			, "-601.9968140590207um",
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
        "Name:="		, "Q5Pad1periphery1",
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
        "Tool Parts:="		, "Q5Pad1periphery1"
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
                "X:="			, "1215.1990769216607um",
                "Y:="			, "-350.0120241677024um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1355.1990325321176um",
                "Y:="			, "-350.12350990720506um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1354.8008691767511um",
                "Y:="			, "-850.1233513731223um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1214.8009135662942um",
                "Y:="			, "-850.0118656336197um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1214.998402590556um",
                "Y:="			, "-602.0119442665247um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1203.9984060783058um",
                "Y:="			, "-602.0031846727067um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1204.0015913851487um",
                "Y:="			, "-598.0031859409793um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1215.0015878973988um",
                "Y:="			, "-598.0119455347974um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1215.1990769216607um",
                "Y:="			, "-350.0120241677024um",
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
        "Name:="		, "Q5Pad2",
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
        "NAME:ThinCondQ5Pad2",
        "Objects:="		, ["Q5Pad2"],
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
                "X:="			, "1215.1990769216607um",
                "Y:="			, "-350.0120241677024um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1355.1990325321176um",
                "Y:="			, "-350.12350990720506um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1354.8008691767511um",
                "Y:="			, "-850.1233513731223um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1214.8009135662942um",
                "Y:="			, "-850.0118656336197um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1214.998402590556um",
                "Y:="			, "-602.0119442665247um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1203.9984060783058um",
                "Y:="			, "-602.0031846727067um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1204.0015913851487um",
                "Y:="			, "-598.0031859409793um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1215.0015878973988um",
                "Y:="			, "-598.0119455347974um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1215.1990769216607um",
                "Y:="			, "-350.0120241677024um",
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
        "Name:="		, "Q5Pad2TrenchComponent",
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
                "X:="			, "1115.2787412995506um",
                "Y:="			, "-249.93242320344564um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1455.2786334963744um",
                "Y:="			, "-250.20317428509486um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1454.7212047988612um",
                "Y:="			, "-950.2029523373791um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1114.7213126020374um",
                "Y:="			, "-949.9322012557299um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1115.2787412995506um",
                "Y:="			, "-249.93242320344564um",
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
        "Name:="		, "Q5Pad2TrenchPeriphery0",
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
                "X:="			, "1204.0015913851487um",
                "Y:="			, "-598.0031859409793um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1215.0015878973988um",
                "Y:="			, "-598.0119455347974um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1214.998402590556um",
                "Y:="			, "-602.0119442665247um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1203.9984060783058um",
                "Y:="			, "-602.0031846727067um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1204.0015913851487um",
                "Y:="			, "-598.0031859409793um",
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
        "Name:="		, "Q5Pad2TrenchPeriphery1",
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
        "Selections:="		, "Q5Pad2TrenchPeriphery0",
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
        "Tool Parts:="		, "Q5Pad2TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q5Pad2TrenchPeriphery1",
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
        "Tool Parts:="		, "Q5Pad2TrenchPeriphery1"
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
                "X:="			, "1115.2787412995506um",
                "Y:="			, "-249.93242320344564um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1455.2786334963744um",
                "Y:="			, "-250.20317428509486um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1454.7212047988612um",
                "Y:="			, "-950.2029523373791um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1114.7213126020374um",
                "Y:="			, "-949.9322012557299um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1115.2787412995506um",
                "Y:="			, "-249.93242320344564um",
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
        "Name:="		, "Q5Pad2periphery0",
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
        "Tool Parts:="		, "Q5Pad2periphery0"
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
                "X:="			, "1204.0015913851487um",
                "Y:="			, "-598.0031859409793um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1215.0015878973988um",
                "Y:="			, "-598.0119455347974um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1214.998402590556um",
                "Y:="			, "-602.0119442665247um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1203.9984060783058um",
                "Y:="			, "-602.0031846727067um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1204.0015913851487um",
                "Y:="			, "-598.0031859409793um",
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
        "Name:="		, "Q5Pad2periphery1",
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
        "Tool Parts:="		, "Q5Pad2periphery1"
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
                "X:="			, "950.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "950.0um",
                "Y:="			, "-1845.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1450.0um",
                "Y:="			, "-1845.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1450.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "-1996.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "-1996.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "950.0um",
                "Y:="			, "-1985.0um",
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
        "Name:="		, "Q6Pad1",
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
        "NAME:ThinCondQ6Pad1",
        "Objects:="		, ["Q6Pad1"],
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
                "X:="			, "950.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "950.0um",
                "Y:="			, "-1845.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1450.0um",
                "Y:="			, "-1845.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1450.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "-1996.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "-1996.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "950.0um",
                "Y:="			, "-1985.0um",
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
        "Name:="		, "Q6Pad1TrenchComponent",
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
                "X:="			, "850.0um",
                "Y:="			, "-2085.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "850.0um",
                "Y:="			, "-1745.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1550.0um",
                "Y:="			, "-1745.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1550.0um",
                "Y:="			, "-2085.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "850.0um",
                "Y:="			, "-2085.0um",
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
        "Name:="		, "Q6Pad1TrenchPeriphery0",
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
                "X:="			, "1198.0um",
                "Y:="			, "-1996.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "-1996.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "-1996.0um",
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
        "Name:="		, "Q6Pad1TrenchPeriphery1",
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
        "Selections:="		, "Q6Pad1TrenchPeriphery0",
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
        "Tool Parts:="		, "Q6Pad1TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q6Pad1TrenchPeriphery1",
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
        "Tool Parts:="		, "Q6Pad1TrenchPeriphery1"
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
                "X:="			, "850.0um",
                "Y:="			, "-2085.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "850.0um",
                "Y:="			, "-1745.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1550.0um",
                "Y:="			, "-1745.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1550.0um",
                "Y:="			, "-2085.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "850.0um",
                "Y:="			, "-2085.0um",
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
        "Name:="		, "Q6Pad1periphery0",
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
        "Tool Parts:="		, "Q6Pad1periphery0"
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
                "X:="			, "1198.0um",
                "Y:="			, "-1996.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "-1996.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "-1996.0um",
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
        "Name:="		, "Q6Pad1periphery1",
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
        "Tool Parts:="		, "Q6Pad1periphery1"
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
                "X:="			, "1450.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1450.0um",
                "Y:="			, "-2155.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "950.0um",
                "Y:="			, "-2155.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "950.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "-2004.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "-2004.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1450.0um",
                "Y:="			, "-2015.0um",
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
        "Name:="		, "Q6Pad2",
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
        "NAME:ThinCondQ6Pad2",
        "Objects:="		, ["Q6Pad2"],
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
                "X:="			, "1450.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1450.0um",
                "Y:="			, "-2155.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "950.0um",
                "Y:="			, "-2155.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "950.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "-2004.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "-2004.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1450.0um",
                "Y:="			, "-2015.0um",
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
        "Name:="		, "Q6Pad2TrenchComponent",
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
                "X:="			, "1550.0um",
                "Y:="			, "-1915.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1550.0um",
                "Y:="			, "-2255.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "850.0um",
                "Y:="			, "-2255.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "850.0um",
                "Y:="			, "-1915.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1550.0um",
                "Y:="			, "-1915.0um",
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
        "Name:="		, "Q6Pad2TrenchPeriphery0",
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
                "X:="			, "1202.0um",
                "Y:="			, "-2004.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "-2004.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "-2004.0um",
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
        "Name:="		, "Q6Pad2TrenchPeriphery1",
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
        "Selections:="		, "Q6Pad2TrenchPeriphery0",
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
        "Tool Parts:="		, "Q6Pad2TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q6Pad2TrenchPeriphery1",
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
        "Tool Parts:="		, "Q6Pad2TrenchPeriphery1"
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
                "X:="			, "1550.0um",
                "Y:="			, "-1915.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1550.0um",
                "Y:="			, "-2255.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "850.0um",
                "Y:="			, "-2255.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "850.0um",
                "Y:="			, "-1915.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1550.0um",
                "Y:="			, "-1915.0um",
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
        "Name:="		, "Q6Pad2periphery0",
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
        "Tool Parts:="		, "Q6Pad2periphery0"
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
                "X:="			, "1202.0um",
                "Y:="			, "-2004.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1198.0um",
                "Y:="			, "-2004.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1202.0um",
                "Y:="			, "-2004.0um",
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
        "Name:="		, "Q6Pad2periphery1",
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
        "Tool Parts:="		, "Q6Pad2periphery1"
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
                "X:="			, "-1450.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1450.0um",
                "Y:="			, "-1845.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-950.0um",
                "Y:="			, "-1845.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-950.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1198.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1198.0um",
                "Y:="			, "-1996.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1202.0um",
                "Y:="			, "-1996.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1202.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1450.0um",
                "Y:="			, "-1985.0um",
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
        "Name:="		, "Q7Pad1",
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
        "NAME:ThinCondQ7Pad1",
        "Objects:="		, ["Q7Pad1"],
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
                "X:="			, "-1450.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1450.0um",
                "Y:="			, "-1845.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-950.0um",
                "Y:="			, "-1845.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-950.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1198.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1198.0um",
                "Y:="			, "-1996.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1202.0um",
                "Y:="			, "-1996.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1202.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1450.0um",
                "Y:="			, "-1985.0um",
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
        "Name:="		, "Q7Pad1TrenchComponent",
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
                "X:="			, "-1550.0um",
                "Y:="			, "-2085.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1550.0um",
                "Y:="			, "-1745.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-850.0um",
                "Y:="			, "-1745.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-850.0um",
                "Y:="			, "-2085.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1550.0um",
                "Y:="			, "-2085.0um",
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
        "Name:="		, "Q7Pad1TrenchPeriphery0",
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
                "X:="			, "-1202.0um",
                "Y:="			, "-1996.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1202.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1198.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1198.0um",
                "Y:="			, "-1996.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1202.0um",
                "Y:="			, "-1996.0um",
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
        "Name:="		, "Q7Pad1TrenchPeriphery1",
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
        "Selections:="		, "Q7Pad1TrenchPeriphery0",
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
        "Tool Parts:="		, "Q7Pad1TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q7Pad1TrenchPeriphery1",
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
        "Tool Parts:="		, "Q7Pad1TrenchPeriphery1"
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
                "X:="			, "-1550.0um",
                "Y:="			, "-2085.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1550.0um",
                "Y:="			, "-1745.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-850.0um",
                "Y:="			, "-1745.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-850.0um",
                "Y:="			, "-2085.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1550.0um",
                "Y:="			, "-2085.0um",
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
        "Name:="		, "Q7Pad1periphery0",
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
        "Tool Parts:="		, "Q7Pad1periphery0"
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
                "X:="			, "-1202.0um",
                "Y:="			, "-1996.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1202.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1198.0um",
                "Y:="			, "-1985.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1198.0um",
                "Y:="			, "-1996.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1202.0um",
                "Y:="			, "-1996.0um",
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
        "Name:="		, "Q7Pad1periphery1",
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
        "Tool Parts:="		, "Q7Pad1periphery1"
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
                "X:="			, "-950.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-950.0um",
                "Y:="			, "-2155.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1450.0um",
                "Y:="			, "-2155.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1450.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1202.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1202.0um",
                "Y:="			, "-2004.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1198.0um",
                "Y:="			, "-2004.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1198.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-950.0um",
                "Y:="			, "-2015.0um",
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
        "Name:="		, "Q7Pad2",
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
        "NAME:ThinCondQ7Pad2",
        "Objects:="		, ["Q7Pad2"],
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
                "X:="			, "-950.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-950.0um",
                "Y:="			, "-2155.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1450.0um",
                "Y:="			, "-2155.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1450.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1202.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1202.0um",
                "Y:="			, "-2004.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1198.0um",
                "Y:="			, "-2004.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1198.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-950.0um",
                "Y:="			, "-2015.0um",
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
        "Name:="		, "Q7Pad2TrenchComponent",
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
                "X:="			, "-850.0um",
                "Y:="			, "-1915.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-850.0um",
                "Y:="			, "-2255.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1550.0um",
                "Y:="			, "-2255.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1550.0um",
                "Y:="			, "-1915.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-850.0um",
                "Y:="			, "-1915.0um",
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
        "Name:="		, "Q7Pad2TrenchPeriphery0",
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
                "X:="			, "-1198.0um",
                "Y:="			, "-2004.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1198.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1202.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1202.0um",
                "Y:="			, "-2004.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1198.0um",
                "Y:="			, "-2004.0um",
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
        "Name:="		, "Q7Pad2TrenchPeriphery1",
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
        "Selections:="		, "Q7Pad2TrenchPeriphery0",
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
        "Tool Parts:="		, "Q7Pad2TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q7Pad2TrenchPeriphery1",
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
        "Tool Parts:="		, "Q7Pad2TrenchPeriphery1"
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
                "X:="			, "-850.0um",
                "Y:="			, "-1915.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-850.0um",
                "Y:="			, "-2255.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1550.0um",
                "Y:="			, "-2255.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1550.0um",
                "Y:="			, "-1915.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-850.0um",
                "Y:="			, "-1915.0um",
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
        "Name:="		, "Q7Pad2periphery0",
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
        "Tool Parts:="		, "Q7Pad2periphery0"
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
                "X:="			, "-1198.0um",
                "Y:="			, "-2004.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1198.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1202.0um",
                "Y:="			, "-2015.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1202.0um",
                "Y:="			, "-2004.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1198.0um",
                "Y:="			, "-2004.0um",
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
        "Name:="		, "Q7Pad2periphery1",
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
        "Tool Parts:="		, "Q7Pad2periphery1"
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
                "X:="			, "-2400.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2400.0um",
                "Y:="			, "4180.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2000.0um",
                "Y:="			, "4180.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2000.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2195.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2195.0um",
                "Y:="			, "4120.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2205.0um",
                "Y:="			, "4120.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2205.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2400.0um",
                "Y:="			, "4170.0um",
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
                "X:="			, "-2400.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2400.0um",
                "Y:="			, "4180.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2000.0um",
                "Y:="			, "4180.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2000.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2195.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2195.0um",
                "Y:="			, "4120.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2205.0um",
                "Y:="			, "4120.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2205.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2400.0um",
                "Y:="			, "4170.0um",
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
                "X:="			, "-2424.0um",
                "Y:="			, "4164.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2424.0um",
                "Y:="			, "4186.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1976.0um",
                "Y:="			, "4186.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1976.0um",
                "Y:="			, "4164.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2424.0um",
                "Y:="			, "4164.0um",
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
                "X:="			, "-2211.0um",
                "Y:="			, "4114.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2211.0um",
                "Y:="			, "4176.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2189.0um",
                "Y:="			, "4176.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2189.0um",
                "Y:="			, "4114.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2211.0um",
                "Y:="			, "4114.0um",
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
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-2424.0um",
                "Y:="			, "4164.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2424.0um",
                "Y:="			, "4186.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1976.0um",
                "Y:="			, "4186.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1976.0um",
                "Y:="			, "4164.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2424.0um",
                "Y:="			, "4164.0um",
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
                "X:="			, "-2211.0um",
                "Y:="			, "4114.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2211.0um",
                "Y:="			, "4176.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2189.0um",
                "Y:="			, "4176.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2189.0um",
                "Y:="			, "4114.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2211.0um",
                "Y:="			, "4114.0um",
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
                "X:="			, "-2149.9999999999914um",
                "Y:="			, "2189.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2149.9999999999914um",
                "Y:="			, "2159.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2249.9999999999914um",
                "Y:="			, "2159.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2249.9999999999914um",
                "Y:="			, "2189.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2204.9999999999914um",
                "Y:="			, "2189.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2204.9999999999914um",
                "Y:="			, "2239.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2194.9999999999914um",
                "Y:="			, "2239.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2194.9999999999914um",
                "Y:="			, "2189.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2149.9999999999914um",
                "Y:="			, "2189.999999999999um",
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
                "X:="			, "-2149.9999999999914um",
                "Y:="			, "2189.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2149.9999999999914um",
                "Y:="			, "2159.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2249.9999999999914um",
                "Y:="			, "2159.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2249.9999999999914um",
                "Y:="			, "2189.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2204.9999999999914um",
                "Y:="			, "2189.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2204.9999999999914um",
                "Y:="			, "2239.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2194.9999999999914um",
                "Y:="			, "2239.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2194.9999999999914um",
                "Y:="			, "2189.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2149.9999999999914um",
                "Y:="			, "2189.999999999999um",
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
                "X:="			, "-2119.9999999999914um",
                "Y:="			, "2219.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2119.9999999999914um",
                "Y:="			, "2129.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2279.9999999999914um",
                "Y:="			, "2129.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2279.9999999999914um",
                "Y:="			, "2219.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2119.9999999999914um",
                "Y:="			, "2219.999999999999um",
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
                "X:="			, "-2188.9999999999914um",
                "Y:="			, "2245.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2188.9999999999914um",
                "Y:="			, "2183.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2210.9999999999914um",
                "Y:="			, "2183.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2210.9999999999914um",
                "Y:="			, "2245.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2188.9999999999914um",
                "Y:="			, "2245.999999999999um",
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
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-2119.9999999999914um",
                "Y:="			, "2219.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2119.9999999999914um",
                "Y:="			, "2129.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2279.9999999999914um",
                "Y:="			, "2129.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2279.9999999999914um",
                "Y:="			, "2219.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2119.9999999999914um",
                "Y:="			, "2219.999999999999um",
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
                "X:="			, "-2188.9999999999914um",
                "Y:="			, "2245.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2188.9999999999914um",
                "Y:="			, "2183.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2210.9999999999914um",
                "Y:="			, "2183.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2210.9999999999914um",
                "Y:="			, "2245.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-2188.9999999999914um",
                "Y:="			, "2245.999999999999um",
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
                "X:="			, "-1600.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1600.0um",
                "Y:="			, "4180.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1200.0um",
                "Y:="			, "4180.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1200.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1395.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1395.0um",
                "Y:="			, "4120.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1405.0um",
                "Y:="			, "4120.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1405.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1600.0um",
                "Y:="			, "4170.0um",
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
                "X:="			, "-1600.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1600.0um",
                "Y:="			, "4180.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1200.0um",
                "Y:="			, "4180.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1200.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1395.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1395.0um",
                "Y:="			, "4120.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1405.0um",
                "Y:="			, "4120.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1405.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1600.0um",
                "Y:="			, "4170.0um",
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
                "X:="			, "-1624.0um",
                "Y:="			, "4164.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1624.0um",
                "Y:="			, "4186.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1176.0um",
                "Y:="			, "4186.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1176.0um",
                "Y:="			, "4164.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1624.0um",
                "Y:="			, "4164.0um",
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
                "X:="			, "-1411.0um",
                "Y:="			, "4114.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1411.0um",
                "Y:="			, "4176.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1389.0um",
                "Y:="			, "4176.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1389.0um",
                "Y:="			, "4114.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1411.0um",
                "Y:="			, "4114.0um",
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
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-1624.0um",
                "Y:="			, "4164.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1624.0um",
                "Y:="			, "4186.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1176.0um",
                "Y:="			, "4186.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1176.0um",
                "Y:="			, "4164.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1624.0um",
                "Y:="			, "4164.0um",
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
                "X:="			, "-1411.0um",
                "Y:="			, "4114.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1411.0um",
                "Y:="			, "4176.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1389.0um",
                "Y:="			, "4176.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1389.0um",
                "Y:="			, "4114.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1411.0um",
                "Y:="			, "4114.0um",
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
                "X:="			, "-1349.9999999999932um",
                "Y:="			, "2189.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1349.9999999999932um",
                "Y:="			, "2159.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1449.9999999999932um",
                "Y:="			, "2159.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1449.9999999999932um",
                "Y:="			, "2189.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1404.9999999999932um",
                "Y:="			, "2189.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1404.9999999999932um",
                "Y:="			, "2239.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1394.9999999999932um",
                "Y:="			, "2239.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1394.9999999999932um",
                "Y:="			, "2189.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1349.9999999999932um",
                "Y:="			, "2189.999999999999um",
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
                "X:="			, "-1349.9999999999932um",
                "Y:="			, "2189.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1349.9999999999932um",
                "Y:="			, "2159.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1449.9999999999932um",
                "Y:="			, "2159.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1449.9999999999932um",
                "Y:="			, "2189.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1404.9999999999932um",
                "Y:="			, "2189.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1404.9999999999932um",
                "Y:="			, "2239.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1394.9999999999932um",
                "Y:="			, "2239.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1394.9999999999932um",
                "Y:="			, "2189.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1349.9999999999932um",
                "Y:="			, "2189.999999999999um",
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
                "X:="			, "-1319.9999999999932um",
                "Y:="			, "2219.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1319.9999999999932um",
                "Y:="			, "2129.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1479.9999999999932um",
                "Y:="			, "2129.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1479.9999999999932um",
                "Y:="			, "2219.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1319.9999999999932um",
                "Y:="			, "2219.999999999999um",
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
                "X:="			, "-1388.9999999999932um",
                "Y:="			, "2245.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1388.9999999999932um",
                "Y:="			, "2183.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1410.9999999999932um",
                "Y:="			, "2183.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1410.9999999999932um",
                "Y:="			, "2245.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1388.9999999999932um",
                "Y:="			, "2245.999999999999um",
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
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-1319.9999999999932um",
                "Y:="			, "2219.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1319.9999999999932um",
                "Y:="			, "2129.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1479.9999999999932um",
                "Y:="			, "2129.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1479.9999999999932um",
                "Y:="			, "2219.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1319.9999999999932um",
                "Y:="			, "2219.999999999999um",
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
                "X:="			, "-1388.9999999999932um",
                "Y:="			, "2245.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1388.9999999999932um",
                "Y:="			, "2183.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1410.9999999999932um",
                "Y:="			, "2183.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1410.9999999999932um",
                "Y:="			, "2245.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1388.9999999999932um",
                "Y:="			, "2245.999999999999um",
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
                "X:="			, "200.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "200.0um",
                "Y:="			, "4180.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "600.0um",
                "Y:="			, "4180.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "600.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "405.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "405.0um",
                "Y:="			, "4120.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "395.0um",
                "Y:="			, "4120.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "395.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "200.0um",
                "Y:="			, "4170.0um",
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
        "Name:="		, "R2Pad1",
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
        "NAME:ThinCondR2Pad1",
        "Objects:="		, ["R2Pad1"],
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
                "X:="			, "200.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "200.0um",
                "Y:="			, "4180.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "600.0um",
                "Y:="			, "4180.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "600.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "405.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "405.0um",
                "Y:="			, "4120.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "395.0um",
                "Y:="			, "4120.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "395.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "200.0um",
                "Y:="			, "4170.0um",
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
        "Name:="		, "R2Pad1TrenchComponent",
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
                "X:="			, "176.0um",
                "Y:="			, "4164.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "176.0um",
                "Y:="			, "4186.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "624.0um",
                "Y:="			, "4186.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "624.0um",
                "Y:="			, "4164.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "176.0um",
                "Y:="			, "4164.0um",
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
        "Name:="		, "R2Pad1TrenchPeriphery0",
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
                "X:="			, "389.0um",
                "Y:="			, "4114.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "389.0um",
                "Y:="			, "4176.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "411.0um",
                "Y:="			, "4176.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "411.0um",
                "Y:="			, "4114.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "389.0um",
                "Y:="			, "4114.0um",
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
        "Name:="		, "R2Pad1TrenchPeriphery1",
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
        "Selections:="		, "R2Pad1TrenchPeriphery0",
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
        "Tool Parts:="		, "R2Pad1TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R2Pad1TrenchPeriphery1",
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
        "Tool Parts:="		, "R2Pad1TrenchPeriphery1"
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
                "X:="			, "176.0um",
                "Y:="			, "4164.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "176.0um",
                "Y:="			, "4186.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "624.0um",
                "Y:="			, "4186.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "624.0um",
                "Y:="			, "4164.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "176.0um",
                "Y:="			, "4164.0um",
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
        "Name:="		, "R2Pad1periphery0",
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
        "Tool Parts:="		, "R2Pad1periphery0"
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
                "X:="			, "389.0um",
                "Y:="			, "4114.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "389.0um",
                "Y:="			, "4176.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "411.0um",
                "Y:="			, "4176.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "411.0um",
                "Y:="			, "4114.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "389.0um",
                "Y:="			, "4114.0um",
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
        "Name:="		, "R2Pad1periphery1",
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
        "Tool Parts:="		, "R2Pad1periphery1"
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
                "X:="			, "450.00000000000534um",
                "Y:="			, "2289.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "450.00000000000534um",
                "Y:="			, "2259.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "350.00000000000534um",
                "Y:="			, "2259.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "350.00000000000534um",
                "Y:="			, "2289.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "395.00000000000534um",
                "Y:="			, "2289.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "395.00000000000534um",
                "Y:="			, "2339.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "405.00000000000534um",
                "Y:="			, "2339.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "405.00000000000534um",
                "Y:="			, "2289.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "450.00000000000534um",
                "Y:="			, "2289.999999999999um",
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
        "Name:="		, "R2Pad2",
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
        "NAME:ThinCondR2Pad2",
        "Objects:="		, ["R2Pad2"],
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
                "X:="			, "450.00000000000534um",
                "Y:="			, "2289.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "450.00000000000534um",
                "Y:="			, "2259.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "350.00000000000534um",
                "Y:="			, "2259.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "350.00000000000534um",
                "Y:="			, "2289.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "395.00000000000534um",
                "Y:="			, "2289.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "395.00000000000534um",
                "Y:="			, "2339.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "405.00000000000534um",
                "Y:="			, "2339.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "405.00000000000534um",
                "Y:="			, "2289.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "450.00000000000534um",
                "Y:="			, "2289.999999999999um",
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
        "Name:="		, "R2Pad2TrenchComponent",
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
                "X:="			, "480.00000000000534um",
                "Y:="			, "2319.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "480.00000000000534um",
                "Y:="			, "2229.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "320.00000000000534um",
                "Y:="			, "2229.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "320.00000000000534um",
                "Y:="			, "2319.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "480.00000000000534um",
                "Y:="			, "2319.999999999999um",
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
        "Name:="		, "R2Pad2TrenchPeriphery0",
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
                "X:="			, "411.00000000000534um",
                "Y:="			, "2345.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "411.00000000000534um",
                "Y:="			, "2283.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "389.00000000000534um",
                "Y:="			, "2283.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "389.00000000000534um",
                "Y:="			, "2345.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "411.00000000000534um",
                "Y:="			, "2345.999999999999um",
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
        "Name:="		, "R2Pad2TrenchPeriphery1",
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
        "Selections:="		, "R2Pad2TrenchPeriphery0",
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
        "Tool Parts:="		, "R2Pad2TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R2Pad2TrenchPeriphery1",
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
        "Tool Parts:="		, "R2Pad2TrenchPeriphery1"
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
                "X:="			, "480.00000000000534um",
                "Y:="			, "2319.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "480.00000000000534um",
                "Y:="			, "2229.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "320.00000000000534um",
                "Y:="			, "2229.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "320.00000000000534um",
                "Y:="			, "2319.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "480.00000000000534um",
                "Y:="			, "2319.999999999999um",
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
        "Name:="		, "R2Pad2periphery0",
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
        "Tool Parts:="		, "R2Pad2periphery0"
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
                "X:="			, "411.00000000000534um",
                "Y:="			, "2345.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "411.00000000000534um",
                "Y:="			, "2283.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "389.00000000000534um",
                "Y:="			, "2283.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "389.00000000000534um",
                "Y:="			, "2345.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "411.00000000000534um",
                "Y:="			, "2345.999999999999um",
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
        "Name:="		, "R2Pad2periphery1",
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
        "Tool Parts:="		, "R2Pad2periphery1"
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
                "X:="			, "1000.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1000.0um",
                "Y:="			, "4180.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1400.0um",
                "Y:="			, "4180.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1400.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1205.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1205.0um",
                "Y:="			, "4120.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1195.0um",
                "Y:="			, "4120.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1195.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1000.0um",
                "Y:="			, "4170.0um",
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
        "Name:="		, "R3Pad1",
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
        "NAME:ThinCondR3Pad1",
        "Objects:="		, ["R3Pad1"],
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
                "X:="			, "1000.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1000.0um",
                "Y:="			, "4180.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1400.0um",
                "Y:="			, "4180.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1400.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1205.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1205.0um",
                "Y:="			, "4120.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1195.0um",
                "Y:="			, "4120.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1195.0um",
                "Y:="			, "4170.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1000.0um",
                "Y:="			, "4170.0um",
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
        "Name:="		, "R3Pad1TrenchComponent",
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
                "X:="			, "976.0um",
                "Y:="			, "4164.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "976.0um",
                "Y:="			, "4186.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1424.0um",
                "Y:="			, "4186.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1424.0um",
                "Y:="			, "4164.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "976.0um",
                "Y:="			, "4164.0um",
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
        "Name:="		, "R3Pad1TrenchPeriphery0",
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
                "X:="			, "1189.0um",
                "Y:="			, "4114.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1189.0um",
                "Y:="			, "4176.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1211.0um",
                "Y:="			, "4176.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1211.0um",
                "Y:="			, "4114.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1189.0um",
                "Y:="			, "4114.0um",
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
        "Name:="		, "R3Pad1TrenchPeriphery1",
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
        "Selections:="		, "R3Pad1TrenchPeriphery0",
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
        "Tool Parts:="		, "R3Pad1TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R3Pad1TrenchPeriphery1",
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
        "Tool Parts:="		, "R3Pad1TrenchPeriphery1"
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
                "X:="			, "976.0um",
                "Y:="			, "4164.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "976.0um",
                "Y:="			, "4186.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1424.0um",
                "Y:="			, "4186.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1424.0um",
                "Y:="			, "4164.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "976.0um",
                "Y:="			, "4164.0um",
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
        "Name:="		, "R3Pad1periphery0",
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
        "Tool Parts:="		, "R3Pad1periphery0"
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
                "X:="			, "1189.0um",
                "Y:="			, "4114.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1189.0um",
                "Y:="			, "4176.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1211.0um",
                "Y:="			, "4176.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1211.0um",
                "Y:="			, "4114.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1189.0um",
                "Y:="			, "4114.0um",
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
        "Name:="		, "R3Pad1periphery1",
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
        "Tool Parts:="		, "R3Pad1periphery1"
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
                "X:="			, "1250.0000000000082um",
                "Y:="			, "2289.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1250.0000000000082um",
                "Y:="			, "2259.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1150.0000000000082um",
                "Y:="			, "2259.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1150.0000000000082um",
                "Y:="			, "2289.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1195.0000000000082um",
                "Y:="			, "2289.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1195.0000000000082um",
                "Y:="			, "2339.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1205.0000000000082um",
                "Y:="			, "2339.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1205.0000000000082um",
                "Y:="			, "2289.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1250.0000000000082um",
                "Y:="			, "2289.999999999999um",
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
        "Name:="		, "R3Pad2",
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
        "NAME:ThinCondR3Pad2",
        "Objects:="		, ["R3Pad2"],
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
                "X:="			, "1250.0000000000082um",
                "Y:="			, "2289.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1250.0000000000082um",
                "Y:="			, "2259.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1150.0000000000082um",
                "Y:="			, "2259.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1150.0000000000082um",
                "Y:="			, "2289.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1195.0000000000082um",
                "Y:="			, "2289.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1195.0000000000082um",
                "Y:="			, "2339.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1205.0000000000082um",
                "Y:="			, "2339.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1205.0000000000082um",
                "Y:="			, "2289.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1250.0000000000082um",
                "Y:="			, "2289.999999999999um",
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
        "Name:="		, "R3Pad2TrenchComponent",
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
                "X:="			, "1280.0000000000082um",
                "Y:="			, "2319.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1280.0000000000082um",
                "Y:="			, "2229.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1120.0000000000082um",
                "Y:="			, "2229.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1120.0000000000082um",
                "Y:="			, "2319.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1280.0000000000082um",
                "Y:="			, "2319.999999999999um",
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
        "Name:="		, "R3Pad2TrenchPeriphery0",
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
                "X:="			, "1211.0000000000082um",
                "Y:="			, "2345.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1211.0000000000082um",
                "Y:="			, "2283.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1189.0000000000082um",
                "Y:="			, "2283.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1189.0000000000082um",
                "Y:="			, "2345.999999999999um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1211.0000000000082um",
                "Y:="			, "2345.999999999999um",
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
        "Name:="		, "R3Pad2TrenchPeriphery1",
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
        "Selections:="		, "R3Pad2TrenchPeriphery0",
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
        "Tool Parts:="		, "R3Pad2TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R3Pad2TrenchPeriphery1",
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
        "Tool Parts:="		, "R3Pad2TrenchPeriphery1"
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
                "X:="			, "1280.0000000000082um",
                "Y:="			, "2319.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1280.0000000000082um",
                "Y:="			, "2229.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1120.0000000000082um",
                "Y:="			, "2229.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1120.0000000000082um",
                "Y:="			, "2319.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1280.0000000000082um",
                "Y:="			, "2319.999999999999um",
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
        "Name:="		, "R3Pad2periphery0",
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
        "Tool Parts:="		, "R3Pad2periphery0"
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
                "X:="			, "1211.0000000000082um",
                "Y:="			, "2345.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1211.0000000000082um",
                "Y:="			, "2283.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1189.0000000000082um",
                "Y:="			, "2283.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1189.0000000000082um",
                "Y:="			, "2345.999999999999um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1211.0000000000082um",
                "Y:="			, "2345.999999999999um",
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
        "Name:="		, "R3Pad2periphery1",
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
        "Tool Parts:="		, "R3Pad2periphery1"
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
                "X:="			, "3374.84042076037um",
                "Y:="			, "800.7883000299928um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3384.840417589688um",
                "Y:="			, "800.7962632971002um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3385.158948273981um",
                "Y:="			, "400.7963901243663um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3375.1589514446628um",
                "Y:="			, "400.78842685725897um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3375.00366773607um",
                "Y:="			, "595.7883650289667um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3325.003683589478um",
                "Y:="			, "595.74854869343um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3324.9957203223707um",
                "Y:="			, "605.7485455227484um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3374.9957044689627um",
                "Y:="			, "605.788361858285um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3374.84042076037um",
                "Y:="			, "800.7883000299928um",
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
        "Name:="		, "R4Pad1",
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
        "NAME:ThinCondR4Pad1",
        "Objects:="		, ["R4Pad1"],
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
                "X:="			, "3374.84042076037um",
                "Y:="			, "800.7883000299928um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3384.840417589688um",
                "Y:="			, "800.7962632971002um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3385.158948273981um",
                "Y:="			, "400.7963901243663um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3375.1589514446628um",
                "Y:="			, "400.78842685725897um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3375.00366773607um",
                "Y:="			, "595.7883650289667um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3325.003683589478um",
                "Y:="			, "595.74854869343um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3324.9957203223707um",
                "Y:="			, "605.7485455227484um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3374.9957044689627um",
                "Y:="			, "605.788361858285um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3374.84042076037um",
                "Y:="			, "800.7883000299928um",
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
        "Name:="		, "R4Pad1TrenchComponent",
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
                "X:="			, "3368.821310821721um",
                "Y:="			, "824.7835144600924um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3390.8213038462213um",
                "Y:="			, "824.8010336477286um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3391.17805821263um",
                "Y:="			, "376.8011756942667um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3369.1780651881295um",
                "Y:="			, "376.78365650663056um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3368.821310821721um",
                "Y:="			, "824.7835144600924um",
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
        "Name:="		, "R4Pad1TrenchPeriphery0",
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
                "X:="			, "3318.9909442645153um",
                "Y:="			, "611.743765660075um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3380.9909246062894um",
                "Y:="			, "611.7931379161405um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3381.0084437939254um",
                "Y:="			, "589.7931448916402um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3319.008463452152um",
                "Y:="			, "589.7437726355747um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3318.9909442645153um",
                "Y:="			, "611.743765660075um",
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
        "Name:="		, "R4Pad1TrenchPeriphery1",
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
        "Selections:="		, "R4Pad1TrenchPeriphery0",
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
        "Tool Parts:="		, "R4Pad1TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R4Pad1TrenchPeriphery1",
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
        "Tool Parts:="		, "R4Pad1TrenchPeriphery1"
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
                "X:="			, "3368.821310821721um",
                "Y:="			, "824.7835144600924um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3390.8213038462213um",
                "Y:="			, "824.8010336477286um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3391.17805821263um",
                "Y:="			, "376.8011756942667um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3369.1780651881295um",
                "Y:="			, "376.78365650663056um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3368.821310821721um",
                "Y:="			, "824.7835144600924um",
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
        "Name:="		, "R4Pad1periphery0",
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
        "Tool Parts:="		, "R4Pad1periphery0"
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
                "X:="			, "3318.9909442645153um",
                "Y:="			, "611.743765660075um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3380.9909246062894um",
                "Y:="			, "611.7931379161405um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3381.0084437939254um",
                "Y:="			, "589.7931448916402um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3319.008463452152um",
                "Y:="			, "589.7437726355747um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3318.9909442645153um",
                "Y:="			, "611.743765660075um",
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
        "Name:="		, "R4Pad1periphery1",
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
        "Tool Parts:="		, "R4Pad1periphery1"
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
                "X:="			, "1395.04013023303um",
                "Y:="			, "549.2116524097819um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1365.0401397450748um",
                "Y:="			, "549.1877626084599um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1364.9605070740015um",
                "Y:="			, "649.1877309016434um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1394.9604975619566um",
                "Y:="			, "649.2116207029653um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1394.9963322639396um",
                "Y:="			, "604.2116349710328um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1444.9963164105313um",
                "Y:="			, "604.2514513065695um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1445.0042796776386um",
                "Y:="			, "594.2514544772511um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1395.0042955310469um",
                "Y:="			, "594.2116381417145um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1395.04013023303um",
                "Y:="			, "549.2116524097819um",
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
        "Name:="		, "R4Pad2",
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
        "NAME:ThinCondR4Pad2",
        "Objects:="		, ["R4Pad2"],
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
                "X:="			, "1395.04013023303um",
                "Y:="			, "549.2116524097819um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1365.0401397450748um",
                "Y:="			, "549.1877626084599um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1364.9605070740015um",
                "Y:="			, "649.1877309016434um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1394.9604975619566um",
                "Y:="			, "649.2116207029653um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1394.9963322639396um",
                "Y:="			, "604.2116349710328um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1444.9963164105313um",
                "Y:="			, "604.2514513065695um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1445.0042796776386um",
                "Y:="			, "594.2514544772511um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1395.0042955310469um",
                "Y:="			, "594.2116381417145um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1395.04013023303um",
                "Y:="			, "549.2116524097819um",
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
        "Name:="		, "R4Pad2TrenchComponent",
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
                "X:="			, "1425.064010522307um",
                "Y:="			, "519.2355517231488um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1335.0640390584417um",
                "Y:="			, "519.1638823191829um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1334.9366267847245um",
                "Y:="			, "679.1638315882765um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1424.9365982485897um",
                "Y:="			, "679.2355009922424um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1425.064010522307um",
                "Y:="			, "519.2355517231488um",
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
        "Name:="		, "R4Pad2TrenchPeriphery0",
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
                "X:="			, "1451.009055735494um",
                "Y:="			, "588.2562343399245um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1389.0090753937202um",
                "Y:="			, "588.206862083859um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1388.9915562060842um",
                "Y:="			, "610.2068551083594um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1450.991536547858um",
                "Y:="			, "610.2562273644248um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1451.009055735494um",
                "Y:="			, "588.2562343399245um",
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
        "Name:="		, "R4Pad2TrenchPeriphery1",
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
        "Selections:="		, "R4Pad2TrenchPeriphery0",
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
        "Tool Parts:="		, "R4Pad2TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R4Pad2TrenchPeriphery1",
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
        "Tool Parts:="		, "R4Pad2TrenchPeriphery1"
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
                "X:="			, "1425.064010522307um",
                "Y:="			, "519.2355517231488um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1335.0640390584417um",
                "Y:="			, "519.1638823191829um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1334.9366267847245um",
                "Y:="			, "679.1638315882765um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1424.9365982485897um",
                "Y:="			, "679.2355009922424um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1425.064010522307um",
                "Y:="			, "519.2355517231488um",
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
        "Name:="		, "R4Pad2periphery0",
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
        "Tool Parts:="		, "R4Pad2periphery0"
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
                "X:="			, "1451.009055735494um",
                "Y:="			, "588.2562343399245um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1389.0090753937202um",
                "Y:="			, "588.206862083859um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1388.9915562060842um",
                "Y:="			, "610.2068551083594um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1450.991536547858um",
                "Y:="			, "610.2562273644248um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1451.009055735494um",
                "Y:="			, "588.2562343399245um",
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
        "Name:="		, "R4Pad2periphery1",
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
        "Tool Parts:="		, "R4Pad2periphery1"
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
                "X:="			, "3374.84042076037um",
                "Y:="			, "-399.2116999700072um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3384.840417589688um",
                "Y:="			, "-399.20373670289985um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3385.158948273981um",
                "Y:="			, "-799.2036098756337um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3375.1589514446628um",
                "Y:="			, "-799.211573142741um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3375.00366773607um",
                "Y:="			, "-604.2116349710333um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3325.003683589478um",
                "Y:="			, "-604.25145130657um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3324.9957203223707um",
                "Y:="			, "-594.2514544772516um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3374.9957044689627um",
                "Y:="			, "-594.211638141715um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3374.84042076037um",
                "Y:="			, "-399.2116999700072um",
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
        "Name:="		, "R5Pad1",
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
        "NAME:ThinCondR5Pad1",
        "Objects:="		, ["R5Pad1"],
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
                "X:="			, "3374.84042076037um",
                "Y:="			, "-399.2116999700072um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3384.840417589688um",
                "Y:="			, "-399.20373670289985um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3385.158948273981um",
                "Y:="			, "-799.2036098756337um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3375.1589514446628um",
                "Y:="			, "-799.211573142741um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3375.00366773607um",
                "Y:="			, "-604.2116349710333um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3325.003683589478um",
                "Y:="			, "-604.25145130657um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3324.9957203223707um",
                "Y:="			, "-594.2514544772516um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3374.9957044689627um",
                "Y:="			, "-594.211638141715um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3374.84042076037um",
                "Y:="			, "-399.2116999700072um",
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
        "Name:="		, "R5Pad1TrenchComponent",
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
                "X:="			, "3368.821310821721um",
                "Y:="			, "-375.2164855399076um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3390.8213038462213um",
                "Y:="			, "-375.19896635227144um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3391.17805821263um",
                "Y:="			, "-823.1988243057333um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3369.1780651881295um",
                "Y:="			, "-823.2163434933694um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3368.821310821721um",
                "Y:="			, "-375.2164855399076um",
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
        "Name:="		, "R5Pad1TrenchPeriphery0",
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
                "X:="			, "3318.9909442645153um",
                "Y:="			, "-588.256234339925um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3380.9909246062894um",
                "Y:="			, "-588.2068620838595um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3381.0084437939254um",
                "Y:="			, "-610.2068551083598um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3319.008463452152um",
                "Y:="			, "-610.2562273644253um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3318.9909442645153um",
                "Y:="			, "-588.256234339925um",
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
        "Name:="		, "R5Pad1TrenchPeriphery1",
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
        "Selections:="		, "R5Pad1TrenchPeriphery0",
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
        "Tool Parts:="		, "R5Pad1TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R5Pad1TrenchPeriphery1",
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
        "Tool Parts:="		, "R5Pad1TrenchPeriphery1"
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
                "X:="			, "3368.821310821721um",
                "Y:="			, "-375.2164855399076um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3390.8213038462213um",
                "Y:="			, "-375.19896635227144um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3391.17805821263um",
                "Y:="			, "-823.1988243057333um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3369.1780651881295um",
                "Y:="			, "-823.2163434933694um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3368.821310821721um",
                "Y:="			, "-375.2164855399076um",
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
        "Name:="		, "R5Pad1periphery0",
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
        "Tool Parts:="		, "R5Pad1periphery0"
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
                "X:="			, "3318.9909442645153um",
                "Y:="			, "-588.256234339925um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3380.9909246062894um",
                "Y:="			, "-588.2068620838595um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3381.0084437939254um",
                "Y:="			, "-610.2068551083598um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3319.008463452152um",
                "Y:="			, "-610.2562273644253um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "3318.9909442645153um",
                "Y:="			, "-588.256234339925um",
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
        "Name:="		, "R5Pad1periphery1",
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
        "Tool Parts:="		, "R5Pad1periphery1"
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
                "X:="			, "1395.04013023303um",
                "Y:="			, "-650.7883475902174um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1365.0401397450748um",
                "Y:="			, "-650.8122373915394um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1364.9605070740015um",
                "Y:="			, "-550.812269098356um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1394.9604975619566um",
                "Y:="			, "-550.788379297034um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1394.9963322639396um",
                "Y:="			, "-595.7883650289665um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1444.9963164105313um",
                "Y:="			, "-595.7485486934298um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1445.0042796776386um",
                "Y:="			, "-605.7485455227483um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1395.0042955310469um",
                "Y:="			, "-605.7883618582848um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1395.04013023303um",
                "Y:="			, "-650.7883475902174um",
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
        "Name:="		, "R5Pad2",
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
        "NAME:ThinCondR5Pad2",
        "Objects:="		, ["R5Pad2"],
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
                "X:="			, "1395.04013023303um",
                "Y:="			, "-650.7883475902174um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1365.0401397450748um",
                "Y:="			, "-650.8122373915394um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1364.9605070740015um",
                "Y:="			, "-550.812269098356um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1394.9604975619566um",
                "Y:="			, "-550.788379297034um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1394.9963322639396um",
                "Y:="			, "-595.7883650289665um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1444.9963164105313um",
                "Y:="			, "-595.7485486934298um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1445.0042796776386um",
                "Y:="			, "-605.7485455227483um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1395.0042955310469um",
                "Y:="			, "-605.7883618582848um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1395.04013023303um",
                "Y:="			, "-650.7883475902174um",
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
        "Name:="		, "R5Pad2TrenchComponent",
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
                "X:="			, "1425.064010522307um",
                "Y:="			, "-680.7644482768505um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1335.0640390584417um",
                "Y:="			, "-680.8361176808164um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1334.9366267847245um",
                "Y:="			, "-520.8361684117228um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1424.9365982485897um",
                "Y:="			, "-520.764499007757um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1425.064010522307um",
                "Y:="			, "-680.7644482768505um",
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
        "Name:="		, "R5Pad2TrenchPeriphery0",
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
                "X:="			, "1451.009055735494um",
                "Y:="			, "-611.7437656600748um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1389.0090753937202um",
                "Y:="			, "-611.7931379161403um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1388.9915562060842um",
                "Y:="			, "-589.7931448916399um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1450.991536547858um",
                "Y:="			, "-589.7437726355745um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1451.009055735494um",
                "Y:="			, "-611.7437656600748um",
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
        "Name:="		, "R5Pad2TrenchPeriphery1",
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
        "Selections:="		, "R5Pad2TrenchPeriphery0",
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
        "Tool Parts:="		, "R5Pad2TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R5Pad2TrenchPeriphery1",
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
        "Tool Parts:="		, "R5Pad2TrenchPeriphery1"
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
                "X:="			, "1425.064010522307um",
                "Y:="			, "-680.7644482768505um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1335.0640390584417um",
                "Y:="			, "-680.8361176808164um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1334.9366267847245um",
                "Y:="			, "-520.8361684117228um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1424.9365982485897um",
                "Y:="			, "-520.764499007757um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1425.064010522307um",
                "Y:="			, "-680.7644482768505um",
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
        "Name:="		, "R5Pad2periphery0",
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
        "Tool Parts:="		, "R5Pad2periphery0"
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
                "X:="			, "1451.009055735494um",
                "Y:="			, "-611.7437656600748um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1389.0090753937202um",
                "Y:="			, "-611.7931379161403um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1388.9915562060842um",
                "Y:="			, "-589.7931448916399um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1450.991536547858um",
                "Y:="			, "-589.7437726355745um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1451.009055735494um",
                "Y:="			, "-611.7437656600748um",
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
        "Name:="		, "R5Pad2periphery1",
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
        "Tool Parts:="		, "R5Pad2periphery1"
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
                "X:="			, "1398.622101572747um",
                "Y:="			, "-3940.3174335276185um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1398.606175043582um",
                "Y:="			, "-3950.317420844894um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "998.6066823525662um",
                "Y:="			, "-3949.6803596782997um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "998.6226088817311um",
                "Y:="			, "-3939.680372361024um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1193.6223615686013um",
                "Y:="			, "-3939.990939679739um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1193.7019942144257um",
                "Y:="			, "-3889.991003093362um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1203.701981531701um",
                "Y:="			, "-3890.006929622527um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1203.6223488858766um",
                "Y:="			, "-3940.006866208904um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1398.622101572747um",
                "Y:="			, "-3940.3174335276185um",
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
        "Name:="		, "R6Pad1",
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
        "NAME:ThinCondR6Pad1",
        "Objects:="		, ["R6Pad1"],
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
                "X:="			, "1398.622101572747um",
                "Y:="			, "-3940.3174335276185um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1398.606175043582um",
                "Y:="			, "-3950.317420844894um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "998.6066823525662um",
                "Y:="			, "-3949.6803596782997um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "998.6226088817311um",
                "Y:="			, "-3939.680372361024um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1193.6223615686013um",
                "Y:="			, "-3939.990939679739um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1193.7019942144257um",
                "Y:="			, "-3889.991003093362um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1203.701981531701um",
                "Y:="			, "-3890.006929622527um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1203.6223488858766um",
                "Y:="			, "-3940.006866208904um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1398.622101572747um",
                "Y:="			, "-3940.3174335276185um",
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
        "Name:="		, "R6Pad1TrenchComponent",
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
                "X:="			, "1422.6316270517068um",
                "Y:="			, "-3934.355664807249um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1422.596588687544um",
                "Y:="			, "-3956.355636905255um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "974.5971568736063um",
                "Y:="			, "-3955.6421283986692um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "974.6321952377691um",
                "Y:="			, "-3933.6421563006634um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1422.6316270517068um",
                "Y:="			, "-3934.355664807249um",
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
        "Name:="		, "R6Pad1TrenchPeriphery0",
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
                "X:="			, "1209.7115298395652um",
                "Y:="			, "-3884.0164931496606um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1209.612785358743um",
                "Y:="			, "-3946.0164145167682um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1187.612813260737um",
                "Y:="			, "-3945.981376152605um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1187.7115577415593um",
                "Y:="			, "-3883.981454785498um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1209.7115298395652um",
                "Y:="			, "-3884.0164931496606um",
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
        "Name:="		, "R6Pad1TrenchPeriphery1",
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
        "Selections:="		, "R6Pad1TrenchPeriphery0",
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
        "Tool Parts:="		, "R6Pad1TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R6Pad1TrenchPeriphery1",
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
        "Tool Parts:="		, "R6Pad1TrenchPeriphery1"
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
                "X:="			, "1422.6316270517068um",
                "Y:="			, "-3934.355664807249um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1422.596588687544um",
                "Y:="			, "-3956.355636905255um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "974.5971568736063um",
                "Y:="			, "-3955.6421283986692um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "974.6321952377691um",
                "Y:="			, "-3933.6421563006634um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1422.6316270517068um",
                "Y:="			, "-3934.355664807249um",
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
        "Name:="		, "R6Pad1periphery0",
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
        "Tool Parts:="		, "R6Pad1periphery0"
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
                "X:="			, "1209.7115298395652um",
                "Y:="			, "-3884.0164931496606um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1209.612785358743um",
                "Y:="			, "-3946.0164145167682um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1187.612813260737um",
                "Y:="			, "-3945.981376152605um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1187.7115577415593um",
                "Y:="			, "-3883.981454785498um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1209.7115298395652um",
                "Y:="			, "-3884.0164931496606um",
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
        "Name:="		, "R6Pad1periphery1",
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
        "Tool Parts:="		, "R6Pad1periphery1"
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
                "X:="			, "1151.3777081863989um",
                "Y:="			, "-2209.921464409862um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1151.4254877738936um",
                "Y:="			, "-2179.921502458036um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1251.4253609466475um",
                "Y:="			, "-2180.080767749684um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1251.3775813591528um",
                "Y:="			, "-2210.0807297015103um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1206.3776384314135um",
                "Y:="			, "-2210.0090603202684um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1206.2980057855893um",
                "Y:="			, "-2260.0089969066457um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1196.2980184683138um",
                "Y:="			, "-2259.9930703774808um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1196.3776511141382um",
                "Y:="			, "-2209.993133791104um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1151.3777081863989um",
                "Y:="			, "-2209.921464409862um",
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
        "Name:="		, "R6Pad2",
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
        "NAME:ThinCondR6Pad2",
        "Objects:="		, ["R6Pad2"],
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
                "X:="			, "1151.3777081863989um",
                "Y:="			, "-2209.921464409862um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1151.4254877738936um",
                "Y:="			, "-2179.921502458036um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1251.4253609466475um",
                "Y:="			, "-2180.080767749684um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1251.3775813591528um",
                "Y:="			, "-2210.0807297015103um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1206.3776384314135um",
                "Y:="			, "-2210.0090603202684um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1206.2980057855893um",
                "Y:="			, "-2260.0089969066457um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1196.2980184683138um",
                "Y:="			, "-2259.9930703774808um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1196.3776511141382um",
                "Y:="			, "-2209.993133791104um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1151.3777081863989um",
                "Y:="			, "-2209.921464409862um",
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
        "Name:="		, "R6Pad2TrenchComponent",
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
                "X:="			, "1121.3299666470782um",
                "Y:="			, "-2239.8736467741933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1121.4733054095618um",
                "Y:="			, "-2149.8737609187147um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1281.4731024859682um",
                "Y:="			, "-2150.128585385353um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1281.3297637234846um",
                "Y:="			, "-2240.1284712408315um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1121.3299666470782um",
                "Y:="			, "-2239.8736467741933um",
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
        "Name:="		, "R6Pad2TrenchPeriphery0",
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
                "X:="			, "1190.2884701604498um",
                "Y:="			, "-2265.983506850347um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1190.3872146412718um",
                "Y:="			, "-2203.9835854832395um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1212.3871867392777um",
                "Y:="			, "-2204.018623847402um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1212.2884422584557um",
                "Y:="			, "-2266.0185452145097um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1190.2884701604498um",
                "Y:="			, "-2265.983506850347um",
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
        "Name:="		, "R6Pad2TrenchPeriphery1",
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
        "Selections:="		, "R6Pad2TrenchPeriphery0",
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
        "Tool Parts:="		, "R6Pad2TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R6Pad2TrenchPeriphery1",
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
        "Tool Parts:="		, "R6Pad2TrenchPeriphery1"
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
                "X:="			, "1121.3299666470782um",
                "Y:="			, "-2239.8736467741933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1121.4733054095618um",
                "Y:="			, "-2149.8737609187147um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1281.4731024859682um",
                "Y:="			, "-2150.128585385353um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1281.3297637234846um",
                "Y:="			, "-2240.1284712408315um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1121.3299666470782um",
                "Y:="			, "-2239.8736467741933um",
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
        "Name:="		, "R6Pad2periphery0",
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
        "Tool Parts:="		, "R6Pad2periphery0"
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
                "X:="			, "1190.2884701604498um",
                "Y:="			, "-2265.983506850347um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1190.3872146412718um",
                "Y:="			, "-2203.9835854832395um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1212.3871867392777um",
                "Y:="			, "-2204.018623847402um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1212.2884422584557um",
                "Y:="			, "-2266.0185452145097um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1190.2884701604498um",
                "Y:="			, "-2265.983506850347um",
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
        "Name:="		, "R6Pad2periphery1",
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
        "Tool Parts:="		, "R6Pad2periphery1"
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
                "X:="			, "-1001.3778984272531um",
                "Y:="			, "-3940.3174335276185um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1001.393824956418um",
                "Y:="			, "-3950.317420844894um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1401.3933176474338um",
                "Y:="			, "-3949.6803596782997um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1401.3773911182689um",
                "Y:="			, "-3939.680372361024um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1206.3776384313987um",
                "Y:="			, "-3939.990939679739um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1206.2980057855743um",
                "Y:="			, "-3889.991003093362um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1196.298018468299um",
                "Y:="			, "-3890.006929622527um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1196.3776511141234um",
                "Y:="			, "-3940.006866208904um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1001.3778984272531um",
                "Y:="			, "-3940.3174335276185um",
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
        "Name:="		, "R7Pad1",
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
        "NAME:ThinCondR7Pad1",
        "Objects:="		, ["R7Pad1"],
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
                "X:="			, "-1001.3778984272531um",
                "Y:="			, "-3940.3174335276185um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1001.393824956418um",
                "Y:="			, "-3950.317420844894um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1401.3933176474338um",
                "Y:="			, "-3949.6803596782997um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1401.3773911182689um",
                "Y:="			, "-3939.680372361024um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1206.3776384313987um",
                "Y:="			, "-3939.990939679739um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1206.2980057855743um",
                "Y:="			, "-3889.991003093362um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1196.298018468299um",
                "Y:="			, "-3890.006929622527um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1196.3776511141234um",
                "Y:="			, "-3940.006866208904um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1001.3778984272531um",
                "Y:="			, "-3940.3174335276185um",
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
        "Name:="		, "R7Pad1TrenchComponent",
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
                "X:="			, "-977.3683729482932um",
                "Y:="			, "-3934.355664807249um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-977.403411312456um",
                "Y:="			, "-3956.355636905255um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1425.4028431263937um",
                "Y:="			, "-3955.6421283986692um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1425.367804762231um",
                "Y:="			, "-3933.6421563006634um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-977.3683729482932um",
                "Y:="			, "-3934.355664807249um",
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
        "Name:="		, "R7Pad1TrenchPeriphery0",
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
                "X:="			, "-1190.2884701604348um",
                "Y:="			, "-3884.0164931496606um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1190.387214641257um",
                "Y:="			, "-3946.0164145167682um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1212.387186739263um",
                "Y:="			, "-3945.981376152605um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1212.2884422584407um",
                "Y:="			, "-3883.981454785498um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1190.2884701604348um",
                "Y:="			, "-3884.0164931496606um",
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
        "Name:="		, "R7Pad1TrenchPeriphery1",
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
        "Selections:="		, "R7Pad1TrenchPeriphery0",
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
        "Tool Parts:="		, "R7Pad1TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R7Pad1TrenchPeriphery1",
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
        "Tool Parts:="		, "R7Pad1TrenchPeriphery1"
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
                "X:="			, "-977.3683729482932um",
                "Y:="			, "-3934.355664807249um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-977.403411312456um",
                "Y:="			, "-3956.355636905255um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1425.4028431263937um",
                "Y:="			, "-3955.6421283986692um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1425.367804762231um",
                "Y:="			, "-3933.6421563006634um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-977.3683729482932um",
                "Y:="			, "-3934.355664807249um",
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
        "Name:="		, "R7Pad1periphery0",
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
        "Tool Parts:="		, "R7Pad1periphery0"
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
                "X:="			, "-1190.2884701604348um",
                "Y:="			, "-3884.0164931496606um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1190.387214641257um",
                "Y:="			, "-3946.0164145167682um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1212.387186739263um",
                "Y:="			, "-3945.981376152605um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1212.2884422584407um",
                "Y:="			, "-3883.981454785498um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1190.2884701604348um",
                "Y:="			, "-3884.0164931496606um",
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
        "Name:="		, "R7Pad1periphery1",
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
        "Tool Parts:="		, "R7Pad1periphery1"
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
                "X:="			, "-1248.622291813602um",
                "Y:="			, "-2209.921464409862um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1248.5745122261073um",
                "Y:="			, "-2179.921502458036um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1148.5746390533534um",
                "Y:="			, "-2180.080767749684um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1148.622418640848um",
                "Y:="			, "-2210.0807297015103um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1193.6223615685874um",
                "Y:="			, "-2210.0090603202684um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1193.7019942144116um",
                "Y:="			, "-2260.0089969066457um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1203.7019815316871um",
                "Y:="			, "-2259.9930703774808um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1203.6223488858627um",
                "Y:="			, "-2209.993133791104um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1248.622291813602um",
                "Y:="			, "-2209.921464409862um",
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
        "Name:="		, "R7Pad2",
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
        "NAME:ThinCondR7Pad2",
        "Objects:="		, ["R7Pad2"],
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
                "X:="			, "-1248.622291813602um",
                "Y:="			, "-2209.921464409862um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1248.5745122261073um",
                "Y:="			, "-2179.921502458036um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1148.5746390533534um",
                "Y:="			, "-2180.080767749684um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1148.622418640848um",
                "Y:="			, "-2210.0807297015103um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1193.6223615685874um",
                "Y:="			, "-2210.0090603202684um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1193.7019942144116um",
                "Y:="			, "-2260.0089969066457um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1203.7019815316871um",
                "Y:="			, "-2259.9930703774808um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1203.6223488858627um",
                "Y:="			, "-2209.993133791104um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1248.622291813602um",
                "Y:="			, "-2209.921464409862um",
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
        "Name:="		, "R7Pad2TrenchComponent",
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
                "X:="			, "-1278.6700333529227um",
                "Y:="			, "-2239.8736467741933um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1278.526694590439um",
                "Y:="			, "-2149.8737609187147um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1118.5268975140327um",
                "Y:="			, "-2150.128585385353um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1118.6702362765163um",
                "Y:="			, "-2240.1284712408315um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1278.6700333529227um",
                "Y:="			, "-2239.8736467741933um",
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
        "Name:="		, "R7Pad2TrenchPeriphery0",
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
                "X:="			, "-1209.711529839551um",
                "Y:="			, "-2265.983506850347um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1209.612785358729um",
                "Y:="			, "-2203.9835854832395um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1187.6128132607232um",
                "Y:="			, "-2204.018623847402um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1187.7115577415452um",
                "Y:="			, "-2266.0185452145097um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1209.711529839551um",
                "Y:="			, "-2265.983506850347um",
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
        "Name:="		, "R7Pad2TrenchPeriphery1",
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
        "Selections:="		, "R7Pad2TrenchPeriphery0",
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
        "Tool Parts:="		, "R7Pad2TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R7Pad2TrenchPeriphery1",
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
        "Tool Parts:="		, "R7Pad2TrenchPeriphery1"
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
                "X:="			, "-1278.6700333529227um",
                "Y:="			, "-2239.8736467741933um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1278.526694590439um",
                "Y:="			, "-2149.8737609187147um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1118.5268975140327um",
                "Y:="			, "-2150.128585385353um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1118.6702362765163um",
                "Y:="			, "-2240.1284712408315um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1278.6700333529227um",
                "Y:="			, "-2239.8736467741933um",
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
        "Name:="		, "R7Pad2periphery0",
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
        "Tool Parts:="		, "R7Pad2periphery0"
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
                "X:="			, "-1209.711529839551um",
                "Y:="			, "-2265.983506850347um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1209.612785358729um",
                "Y:="			, "-2203.9835854832395um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1187.6128132607232um",
                "Y:="			, "-2204.018623847402um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1187.7115577415452um",
                "Y:="			, "-2266.0185452145097um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1209.711529839551um",
                "Y:="			, "-2265.983506850347um",
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
        "Name:="		, "R7Pad2periphery1",
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
        "Tool Parts:="		, "R7Pad2periphery1"
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
        "Selections:="		, "Q2Pad1TrenchComponent",
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
        "Selections:="		, "S0,Q2Pad1TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q2Pad2TrenchComponent",
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
        "Selections:="		, "S0,Q2Pad2TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q3Pad1TrenchComponent",
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
        "Selections:="		, "S0,Q3Pad1TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q3Pad2TrenchComponent",
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
        "Selections:="		, "S0,Q3Pad2TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q4Pad1TrenchComponent",
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
        "Selections:="		, "S0,Q4Pad1TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q4Pad2TrenchComponent",
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
        "Selections:="		, "S0,Q4Pad2TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q5Pad1TrenchComponent",
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
        "Selections:="		, "S0,Q5Pad1TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q5Pad2TrenchComponent",
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
        "Selections:="		, "S0,Q5Pad2TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q6Pad1TrenchComponent",
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
        "Selections:="		, "S0,Q6Pad1TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q6Pad2TrenchComponent",
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
        "Selections:="		, "S0,Q6Pad2TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q7Pad1TrenchComponent",
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
        "Selections:="		, "S0,Q7Pad1TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q7Pad2TrenchComponent",
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
        "Selections:="		, "S0,Q7Pad2TrenchComponent"
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
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R2Pad1TrenchComponent",
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
        "Selections:="		, "S0,R2Pad1TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R2Pad2TrenchComponent",
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
        "Selections:="		, "S0,R2Pad2TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R3Pad1TrenchComponent",
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
        "Selections:="		, "S0,R3Pad1TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R3Pad2TrenchComponent",
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
        "Selections:="		, "S0,R3Pad2TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R4Pad1TrenchComponent",
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
        "Selections:="		, "S0,R4Pad1TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R4Pad2TrenchComponent",
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
        "Selections:="		, "S0,R4Pad2TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R5Pad1TrenchComponent",
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
        "Selections:="		, "S0,R5Pad1TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R5Pad2TrenchComponent",
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
        "Selections:="		, "S0,R5Pad2TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R6Pad1TrenchComponent",
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
        "Selections:="		, "S0,R6Pad1TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R6Pad2TrenchComponent",
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
        "Selections:="		, "S0,R6Pad2TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R7Pad1TrenchComponent",
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
        "Selections:="		, "S0,R7Pad1TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R7Pad2TrenchComponent",
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
        "Selections:="		, "S0,R7Pad2TrenchComponent"
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
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q0Pad1",
        "Objects:="		, ["Q0Pad1"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q0Pad2",
        "Objects:="		, ["Q0Pad2"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q1Pad1",
        "Objects:="		, ["Q1Pad1"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q1Pad2",
        "Objects:="		, ["Q1Pad2"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q2Pad1",
        "Objects:="		, ["Q2Pad1"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q2Pad2",
        "Objects:="		, ["Q2Pad2"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q3Pad1",
        "Objects:="		, ["Q3Pad1"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q3Pad2",
        "Objects:="		, ["Q3Pad2"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q4Pad1",
        "Objects:="		, ["Q4Pad1"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q4Pad2",
        "Objects:="		, ["Q4Pad2"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q5Pad1",
        "Objects:="		, ["Q5Pad1"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q5Pad2",
        "Objects:="		, ["Q5Pad2"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q6Pad1",
        "Objects:="		, ["Q6Pad1"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q6Pad2",
        "Objects:="		, ["Q6Pad2"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q7Pad1",
        "Objects:="		, ["Q7Pad1"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q7Pad2",
        "Objects:="		, ["Q7Pad2"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R0Pad1",
        "Objects:="		, ["R0Pad1"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R0Pad2",
        "Objects:="		, ["R0Pad2"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R1Pad1",
        "Objects:="		, ["R1Pad1"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R1Pad2",
        "Objects:="		, ["R1Pad2"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R2Pad1",
        "Objects:="		, ["R2Pad1"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R2Pad2",
        "Objects:="		, ["R2Pad2"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R3Pad1",
        "Objects:="		, ["R3Pad1"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R3Pad2",
        "Objects:="		, ["R3Pad2"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R4Pad1",
        "Objects:="		, ["R4Pad1"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R4Pad2",
        "Objects:="		, ["R4Pad2"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R5Pad1",
        "Objects:="		, ["R5Pad1"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R5Pad2",
        "Objects:="		, ["R5Pad2"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R6Pad1",
        "Objects:="		, ["R6Pad1"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R6Pad2",
        "Objects:="		, ["R6Pad2"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R7Pad1",
        "Objects:="		, ["R7Pad1"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R7Pad2",
        "Objects:="		, ["R7Pad2"]
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
oDesign.ExportMatrixData(r"C:\Users\jhoward\Desktop\8Q\capMat\capMatExtractor_Results.csv", "C", "", "capSim:LastAdaptive", "Original", "ohm", "nH", "pF", "mSie", 5000000000, "Maxwell,Spice,Couple", 0, False, 5, 8, 0)
oProject.Save()
