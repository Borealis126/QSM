$begin 'Profile'
	$begin '56001'
		$begin 'ProfileGroup'
			MajorVer=2021
			MinorVer=1
			Name='Solution Process'
			StartInfo='Time:  05/15/2021 20:29:19; Host: c008; Processor: 36; OS: Linux 3.10.0-1160.15.2.el7.x86_64; Q3D 2021.1.0'
			TotalInfo='Elapsed time : 00:01:31 , ComEngine Memory : 99.8 M'
			GroupOptions=2
			TaskDataOptions(Memory=8)
			$begin 'ProfileGroup'
				MajorVer=2021
				MinorVer=1
				Name='Initialization'
				StartInfo='Time:  05/15/2021 20:29:19'
				TotalInfo='Elapsed time : 00:00:00'
				GroupOptions=1
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'Executing from /sw/apps/ansys/ansysEM/AnsysEM21.1/Linux64/Q3DCOMENGINE.exe\')', false, true)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'HPC Enabled\')', false, true)
			$end 'ProfileGroup'
			$begin 'ProfileGroup'
				MajorVer=2021
				MinorVer=1
				Name='Initial Meshing'
				StartInfo='Time:  05/15/2021 20:29:19'
				TotalInfo='Elapsed time : 00:00:02'
				GroupOptions=0
				TaskDataOptions(Memory=8)
				ProfileItem('  Mesh (phi surface)', 1, 0, 0, 0, 57304, 'I(1, 0, \'772 triangles\')', true, true)
			$end 'ProfileGroup'
			$begin 'ProfileGroup'
				MajorVer=2021
				MinorVer=1
				Name='Adaptive Meshing'
				StartInfo='Time:  05/15/2021 20:29:22'
				TotalInfo='Elapsed time : 00:01:28'
				GroupOptions=124
				TaskDataOptions()
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 1'
					StartInfo='Time:  05/15/2021 20:29:22'
					TotalInfo='Elapsed time : 00:00:03'
					GroupOptions=2853898800
					TaskDataOptions()
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c008 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 1, 0, 4, 0, 283304, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 1, 0, 283304, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 2'
					StartInfo='Time:  05/15/2021 20:29:25'
					TotalInfo='Elapsed time : 00:00:03'
					GroupOptions=2853898800
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 57496, 'I(1, 0, \'2142 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c008 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 0, 0, 7, 0, 451200, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 1, 0, 451200, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 3'
					StartInfo='Time:  05/15/2021 20:29:29'
					TotalInfo='Elapsed time : 00:00:03'
					GroupOptions=2853898800
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 57520, 'I(1, 0, \'4630 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c008 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 1, 0, 13, 0, 642868, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 2, 0, 642868, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 4'
					StartInfo='Time:  05/15/2021 20:29:32'
					TotalInfo='Elapsed time : 00:00:04'
					GroupOptions=2853898800
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 57592, 'I(1, 0, \'9600 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c008 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 1, 0, 19, 0, 695404, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 1, 0, 6, 0, 695404, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 5'
					StartInfo='Time:  05/15/2021 20:29:37'
					TotalInfo='Elapsed time : 00:00:06'
					GroupOptions=2853898800
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 1, 0, 0, 0, 70400, 'I(1, 0, \'19852 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c008 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 2, 0, 34, 0, 934232, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 1, 0, 15, 0, 934232, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 6'
					StartInfo='Time:  05/15/2021 20:29:43'
					TotalInfo='Elapsed time : 00:00:10'
					GroupOptions=124
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 1, 0, 1, 0, 109836, 'I(1, 0, \'39680 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c008 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 4, 0, 56, 0, 993236, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 2, 0, 36, 0, 1061064, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 7'
					StartInfo='Time:  05/15/2021 20:29:53'
					TotalInfo='Elapsed time : 00:00:18'
					GroupOptions=2853898800
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 2, 0, 2, 0, 183312, 'I(1, 0, \'76762 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c008 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 7, 0, 85, 0, 1333776, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 6, 0, 87, 0, 1639356, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 8'
					StartInfo='Time:  05/15/2021 20:30:12'
					TotalInfo='Elapsed time : 00:00:38'
					GroupOptions=124
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 4, 0, 4, 0, 315984, 'I(1, 0, \'143178 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c008 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 19, 0, 258, 0, 3082228, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 11, 0, 163, 0, 3453736, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				ProfileFootnote('I(1, 0, \'Adaptive Passes converged\')', 0)
			$end 'ProfileGroup'
			ProfileFootnote('I(1, 0, \'Time:  05/15/2021 20:30:51, Status: Normal Completion\')', 0)
		$end 'ProfileGroup'
	$end '56001'
$end 'Profile'
