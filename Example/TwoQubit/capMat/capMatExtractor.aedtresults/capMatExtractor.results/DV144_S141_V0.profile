$begin 'Profile'
	$begin '56001'
		$begin 'ProfileGroup'
			MajorVer=2022
			MinorVer=1
			Name='Solution Process'
			StartInfo='Time:  08/18/2022 13:39:34; Host: LABWIN002; Processor: 44; OS: NT 6.3; Q3D 2022.1.0'
			TotalInfo='Elapsed time : 00:07:22 , ComEngine Memory : 70.8 M'
			GroupOptions=2
			TaskDataOptions(Memory=8)
			$begin 'ProfileGroup'
				MajorVer=2022
				MinorVer=1
				Name='Initialization'
				StartInfo='Time:  08/18/2022 13:39:34'
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
				StartInfo='Time:  08/18/2022 13:39:34'
				TotalInfo='Elapsed time : 00:00:00'
				GroupOptions=0
				TaskDataOptions(Memory=8)
				ProfileItem('  Mesh (phi surface)', 0, 0, 0, 0, 36260, 'I(1, 0, \'646 triangles\')', true, true)
			$end 'ProfileGroup'
			$begin 'ProfileGroup'
				MajorVer=2022
				MinorVer=1
				Name='Adaptive Meshing'
				StartInfo='Time:  08/18/2022 13:39:35'
				TotalInfo='Elapsed time : 00:07:21'
				GroupOptions=3433280
				TaskDataOptions()
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 1'
					StartInfo='Time:  08/18/2022 13:39:35'
					TotalInfo='Elapsed time : 00:00:03'
					GroupOptions=3433280
					TaskDataOptions()
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 0, 0, 1, 0, 46084, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 0, 0, 46084, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 2'
					StartInfo='Time:  08/18/2022 13:39:39'
					TotalInfo='Elapsed time : 00:00:05'
					GroupOptions=3433280
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 31048, 'I(1, 0, \'1730 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 2, 0, 6, 0, 136708, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 1, 0, 136708, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 3'
					StartInfo='Time:  08/18/2022 13:39:45'
					TotalInfo='Elapsed time : 00:00:07'
					GroupOptions=3433280
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 35632, 'I(1, 0, \'3742 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 3, 0, 12, 0, 154140, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 0, 0, 154140, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 4'
					StartInfo='Time:  08/18/2022 13:39:52'
					TotalInfo='Elapsed time : 00:00:09'
					GroupOptions=3433280
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 44556, 'I(1, 0, \'7954 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 3, 0, 14, 0, 129916, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 1, 0, 3, 0, 132040, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 5'
					StartInfo='Time:  08/18/2022 13:40:01'
					TotalInfo='Elapsed time : 00:00:22'
					GroupOptions=3433280
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 1, 0, 1, 0, 61984, 'I(1, 0, \'16352 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 15, 0, 58, 0, 387124, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 1, 0, 7, 0, 387124, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 6'
					StartInfo='Time:  08/18/2022 13:40:23'
					TotalInfo='Elapsed time : 00:00:39'
					GroupOptions=3433280
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 1, 0, 1, 0, 93836, 'I(1, 0, \'32236 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 28, 0, 110, 0, 708512, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 5, 0, 19, 0, 708512, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 7'
					StartInfo='Time:  08/18/2022 13:41:03'
					TotalInfo='Elapsed time : 00:01:06'
					GroupOptions=3433280
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 4, 0, 4, 0, 151932, 'I(1, 0, \'60630 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 44, 0, 172, 0, 993056, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 12, 0, 45, 0, 1080252, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 8'
					StartInfo='Time:  08/18/2022 13:42:09'
					TotalInfo='Elapsed time : 00:01:46'
					GroupOptions=3433280
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 8, 0, 8, 0, 260004, 'I(1, 0, \'111530 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 63, 0, 234, 0, 1398428, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 28, 0, 114, 0, 1587052, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 9'
					StartInfo='Time:  08/18/2022 13:43:56'
					TotalInfo='Elapsed time : 00:02:59'
					GroupOptions=3433280
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 14, 0, 14, 0, 443528, 'I(1, 0, \'198620 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 87, 0, 321, 0, 1753072, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 68, 0, 268, 0, 2154592, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				ProfileFootnote('I(1, 0, \'Adaptive Passes converged\')', 0)
			$end 'ProfileGroup'
			$begin 'ProfileGroup'
				MajorVer=2022
				MinorVer=1
				Name='Frequency Sweep'
				StartInfo='Time:  08/18/2022 13:46:56'
				TotalInfo='Elapsed time : 00:00:00'
				GroupOptions=3433280
				TaskDataOptions()
			$end 'ProfileGroup'
			ProfileFootnote('I(1, 0, \'Time:  08/18/2022 13:46:56, Status: Normal Completion\')', 0)
		$end 'ProfileGroup'
	$end '56001'
$end 'Profile'
