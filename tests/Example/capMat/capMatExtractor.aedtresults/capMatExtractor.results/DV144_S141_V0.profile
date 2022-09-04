$begin 'Profile'
	$begin '56001'
		$begin 'ProfileGroup'
			MajorVer=2022
			MinorVer=1
			Name='Solution Process'
			StartInfo='Time:  09/04/2022 16:35:03; Host: LABWIN002; Processor: 44; OS: NT 6.3; Q3D 2022.1.0'
			TotalInfo='Elapsed time : 00:06:23 , ComEngine Memory : 70.8 M'
			GroupOptions=2
			TaskDataOptions(Memory=8)
			$begin 'ProfileGroup'
				MajorVer=2022
				MinorVer=1
				Name='Initialization'
				StartInfo='Time:  09/04/2022 16:35:03'
				TotalInfo='Elapsed time : 00:00:00'
				GroupOptions=1
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'Executing from C:\\\\Program Files\\\\AnsysEM\\\\v221\\\\Win64\\\\Q3DCOMENGINE.exe\')', false, true)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'HPC Enabled\')', false, true)
			$end 'ProfileGroup'
			$begin 'ProfileGroup'
				MajorVer=2022
				MinorVer=1
				Name='Initial Meshing'
				StartInfo='Time:  09/04/2022 16:35:03'
				TotalInfo='Elapsed time : 00:00:00'
				GroupOptions=0
				TaskDataOptions(Memory=8)
				ProfileItem('  Mesh (phi surface)', 0, 0, 0, 0, 36404, 'I(1, 0, \'646 triangles\')', true, true)
			$end 'ProfileGroup'
			$begin 'ProfileGroup'
				MajorVer=2022
				MinorVer=1
				Name='Adaptive Meshing'
				StartInfo='Time:  09/04/2022 16:35:04'
				TotalInfo='Elapsed time : 00:06:22'
				GroupOptions=4091248
				TaskDataOptions()
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 1'
					StartInfo='Time:  09/04/2022 16:35:04'
					TotalInfo='Elapsed time : 00:00:03'
					GroupOptions=4091248
					TaskDataOptions()
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 0, 0, 1, 0, 44284, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 0, 0, 44284, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 2'
					StartInfo='Time:  09/04/2022 16:35:08'
					TotalInfo='Elapsed time : 00:00:05'
					GroupOptions=4091248
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 31160, 'I(1, 0, \'1730 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 2, 0, 6, 0, 137596, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 0, 0, 137596, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 3'
					StartInfo='Time:  09/04/2022 16:35:13'
					TotalInfo='Elapsed time : 00:00:06'
					GroupOptions=4091248
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 35720, 'I(1, 0, \'3742 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 3, 0, 11, 0, 154288, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 1, 0, 154288, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 4'
					StartInfo='Time:  09/04/2022 16:35:20'
					TotalInfo='Elapsed time : 00:00:08'
					GroupOptions=4091248
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 44768, 'I(1, 0, \'7954 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 3, 0, 14, 0, 131252, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 1, 0, 2, 0, 133072, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 5'
					StartInfo='Time:  09/04/2022 16:35:28'
					TotalInfo='Elapsed time : 00:00:20'
					GroupOptions=4091248
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 62192, 'I(1, 0, \'16352 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 14, 0, 55, 0, 392928, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 1, 0, 6, 0, 392928, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 6'
					StartInfo='Time:  09/04/2022 16:35:49'
					TotalInfo='Elapsed time : 00:00:37'
					GroupOptions=4091248
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 1, 0, 1, 0, 94236, 'I(1, 0, \'32236 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 27, 0, 108, 0, 712864, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 4, 0, 15, 0, 712864, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 7'
					StartInfo='Time:  09/04/2022 16:36:26'
					TotalInfo='Elapsed time : 00:00:59'
					GroupOptions=4091248
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 3, 0, 3, 0, 152300, 'I(1, 0, \'60630 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 43, 0, 167, 0, 993952, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 8, 0, 31, 0, 1080944, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 8'
					StartInfo='Time:  09/04/2022 16:37:26'
					TotalInfo='Elapsed time : 00:01:30'
					GroupOptions=4091248
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 6, 0, 6, 0, 260240, 'I(1, 0, \'111530 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 59, 0, 224, 0, 1399656, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 19, 0, 74, 0, 1586724, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 9'
					StartInfo='Time:  09/04/2022 16:38:56'
					TotalInfo='Elapsed time : 00:02:30'
					GroupOptions=4091248
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 11, 0, 11, 0, 443608, 'I(1, 0, \'198620 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 80, 0, 293, 0, 1753972, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 49, 0, 195, 0, 2155788, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				ProfileFootnote('I(1, 0, \'Adaptive Passes converged\')', 0)
			$end 'ProfileGroup'
			$begin 'ProfileGroup'
				MajorVer=2022
				MinorVer=1
				Name='Frequency Sweep'
				StartInfo='Time:  09/04/2022 16:41:27'
				TotalInfo='Elapsed time : 00:00:00'
				GroupOptions=4091248
				TaskDataOptions()
			$end 'ProfileGroup'
			ProfileFootnote('I(1, 0, \'Time:  09/04/2022 16:41:27, Status: Normal Completion\')', 0)
		$end 'ProfileGroup'
	$end '56001'
$end 'Profile'
