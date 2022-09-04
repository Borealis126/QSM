$begin 'Profile'
	$begin '56001'
		$begin 'ProfileGroup'
			MajorVer=2022
			MinorVer=1
			Name='Solution Process'
			StartInfo='Time:  08/31/2022 23:09:32; Host: LABWIN002; Processor: 44; OS: NT 6.3; Q3D 2022.1.0'
			TotalInfo='Elapsed time : 00:06:20 , ComEngine Memory : 71.3 M'
			GroupOptions=2
			TaskDataOptions(Memory=8)
			$begin 'ProfileGroup'
				MajorVer=2022
				MinorVer=1
				Name='Initialization'
				StartInfo='Time:  08/31/2022 23:09:32'
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
				StartInfo='Time:  08/31/2022 23:09:32'
				TotalInfo='Elapsed time : 00:00:00'
				GroupOptions=0
				TaskDataOptions(Memory=8)
				ProfileItem('  Mesh (phi surface)', 0, 0, 0, 0, 36376, 'I(1, 0, \'646 triangles\')', true, true)
			$end 'ProfileGroup'
			$begin 'ProfileGroup'
				MajorVer=2022
				MinorVer=1
				Name='Adaptive Meshing'
				StartInfo='Time:  08/31/2022 23:09:33'
				TotalInfo='Elapsed time : 00:06:19'
				GroupOptions=3575856
				TaskDataOptions()
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 1'
					StartInfo='Time:  08/31/2022 23:09:33'
					TotalInfo='Elapsed time : 00:00:03'
					GroupOptions=3575856
					TaskDataOptions()
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 0, 0, 1, 0, 44816, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 0, 0, 44816, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 2'
					StartInfo='Time:  08/31/2022 23:09:36'
					TotalInfo='Elapsed time : 00:00:05'
					GroupOptions=3575856
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 31116, 'I(1, 0, \'1730 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 2, 0, 6, 0, 137612, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 1, 0, 137612, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 3'
					StartInfo='Time:  08/31/2022 23:09:42'
					TotalInfo='Elapsed time : 00:00:06'
					GroupOptions=3575856
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 35632, 'I(1, 0, \'3742 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 3, 0, 11, 0, 156752, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 1, 0, 156752, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 4'
					StartInfo='Time:  08/31/2022 23:09:49'
					TotalInfo='Elapsed time : 00:00:08'
					GroupOptions=3575856
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 44652, 'I(1, 0, \'7954 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 3, 0, 14, 0, 130688, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 1, 0, 2, 0, 132296, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 5'
					StartInfo='Time:  08/31/2022 23:09:57'
					TotalInfo='Elapsed time : 00:00:20'
					GroupOptions=3575856
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 62180, 'I(1, 0, \'16352 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 14, 0, 55, 0, 392128, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 1, 0, 6, 0, 392128, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 6'
					StartInfo='Time:  08/31/2022 23:10:17'
					TotalInfo='Elapsed time : 00:00:37'
					GroupOptions=3575856
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 1, 0, 1, 0, 94236, 'I(1, 0, \'32236 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 27, 0, 108, 0, 710652, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 4, 0, 15, 0, 710652, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 7'
					StartInfo='Time:  08/31/2022 23:10:54'
					TotalInfo='Elapsed time : 00:00:59'
					GroupOptions=3575856
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 3, 0, 3, 0, 152088, 'I(1, 0, \'60630 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 43, 0, 167, 0, 995516, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 8, 0, 32, 0, 1082056, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 8'
					StartInfo='Time:  08/31/2022 23:11:54'
					TotalInfo='Elapsed time : 00:01:30'
					GroupOptions=3575856
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 6, 0, 6, 0, 260048, 'I(1, 0, \'111530 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 59, 0, 224, 0, 1401208, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 18, 0, 74, 0, 1587616, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 9'
					StartInfo='Time:  08/31/2022 23:13:25'
					TotalInfo='Elapsed time : 00:02:28'
					GroupOptions=3575856
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 11, 0, 11, 0, 443096, 'I(1, 0, \'198620 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 79, 0, 292, 0, 1753548, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 48, 0, 190, 0, 2155140, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				ProfileFootnote('I(1, 0, \'Adaptive Passes converged\')', 0)
			$end 'ProfileGroup'
			$begin 'ProfileGroup'
				MajorVer=2022
				MinorVer=1
				Name='Frequency Sweep'
				StartInfo='Time:  08/31/2022 23:15:53'
				TotalInfo='Elapsed time : 00:00:00'
				GroupOptions=3575856
				TaskDataOptions()
			$end 'ProfileGroup'
			ProfileFootnote('I(1, 0, \'Time:  08/31/2022 23:15:53, Status: Normal Completion\')', 0)
		$end 'ProfileGroup'
	$end '56001'
$end 'Profile'
