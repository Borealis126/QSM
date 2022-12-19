$begin 'Profile'
	$begin '56001'
		$begin 'ProfileGroup'
			MajorVer=2022
			MinorVer=1
			Name='Solution Process'
			StartInfo='Time:  12/18/2022 22:50:59; Host: LABWIN002; Processor: 44; OS: NT 6.3; Q3D 2022.1.0'
			TotalInfo='Elapsed time : 00:42:57 , ComEngine Memory : 99.5 M'
			GroupOptions=2
			TaskDataOptions(Memory=8)
			$begin 'ProfileGroup'
				MajorVer=2022
				MinorVer=1
				Name='Initialization'
				StartInfo='Time:  12/18/2022 22:50:59'
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
				StartInfo='Time:  12/18/2022 22:50:59'
				TotalInfo='Elapsed time : 00:00:04'
				GroupOptions=0
				TaskDataOptions(Memory=8)
				ProfileItem('  Mesh (phi surface)', 1, 0, 1, 0, 52708, 'I(1, 0, \'2682 triangles\')', true, true)
			$end 'ProfileGroup'
			$begin 'ProfileGroup'
				MajorVer=2022
				MinorVer=1
				Name='Adaptive Meshing'
				StartInfo='Time:  12/18/2022 22:51:03'
				TotalInfo='Elapsed time : 00:42:53'
				GroupOptions=3434496
				TaskDataOptions()
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 1'
					StartInfo='Time:  12/18/2022 22:51:03'
					TotalInfo='Elapsed time : 00:00:04'
					GroupOptions=3434496
					TaskDataOptions()
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 0, 0, 2, 0, 48252, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 1, 0, 49760, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 2'
					StartInfo='Time:  12/18/2022 22:51:08'
					TotalInfo='Elapsed time : 00:00:06'
					GroupOptions=3434496
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 43492, 'I(1, 0, \'5340 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 2, 0, 8, 0, 89148, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 1, 0, 89148, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 3'
					StartInfo='Time:  12/18/2022 22:51:14'
					TotalInfo='Elapsed time : 00:00:14'
					GroupOptions=3434496
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 56012, 'I(1, 0, \'11152 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 8, 0, 34, 0, 253836, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 2, 0, 4, 0, 253836, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 4'
					StartInfo='Time:  12/18/2022 22:51:28'
					TotalInfo='Elapsed time : 00:00:34'
					GroupOptions=3434496
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 1, 0, 1, 0, 81556, 'I(1, 0, \'24074 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 25, 0, 96, 0, 599156, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 4, 0, 17, 0, 602400, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 5'
					StartInfo='Time:  12/18/2022 22:52:03'
					TotalInfo='Elapsed time : 00:01:00'
					GroupOptions=3434496
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 3, 0, 3, 0, 134392, 'I(1, 0, \'50106 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 33, 0, 130, 0, 776312, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 20, 0, 77, 0, 836268, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 6'
					StartInfo='Time:  12/18/2022 22:53:03'
					TotalInfo='Elapsed time : 00:02:18'
					GroupOptions=3434496
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 6, 0, 6, 0, 244268, 'I(1, 0, \'102484 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 70, 0, 269, 0, 1567760, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 55, 0, 223, 0, 1724332, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 7'
					StartInfo='Time:  12/18/2022 22:55:22'
					TotalInfo='Elapsed time : 00:04:48'
					GroupOptions=3434496
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 11, 0, 11, 0, 439076, 'I(1, 0, \'194748 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 111, 0, 422, 0, 2506452, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 156, 0, 624, 0, 2857016, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 8'
					StartInfo='Time:  12/18/2022 23:00:10'
					TotalInfo='Elapsed time : 00:10:37'
					GroupOptions=3434496
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 21, 0, 21, 0, 768748, 'I(1, 0, \'353602 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 172, 0, 638, 0, 3558216, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 429, 0, 1717, 0, 4312224, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2022
					MinorVer=1
					Name='Pass 9'
					StartInfo='Time:  12/18/2022 23:10:48'
					TotalInfo='Elapsed time : 00:23:09'
					GroupOptions=3434496
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 40, 0, 40, 0, 1399108, 'I(1, 0, \'633706 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'labwin002 Using 4 core(s); 805173364 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 245, 0, 878, 0, 4737676, 'I(1, 0, \'4 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 1079, 0, 4310, 0, 6313216, 'I(1, 0, \'4 core(s)\')', true, true)
				$end 'ProfileGroup'
				ProfileFootnote('I(1, 0, \'Adaptive Passes converged\')', 0)
			$end 'ProfileGroup'
			$begin 'ProfileGroup'
				MajorVer=2022
				MinorVer=1
				Name='Frequency Sweep'
				StartInfo='Time:  12/18/2022 23:33:57'
				TotalInfo='Elapsed time : 00:00:00'
				GroupOptions=3434496
				TaskDataOptions()
			$end 'ProfileGroup'
			ProfileFootnote('I(1, 0, \'Time:  12/18/2022 23:33:57, Status: Normal Completion\')', 0)
		$end 'ProfileGroup'
	$end '56001'
$end 'Profile'
