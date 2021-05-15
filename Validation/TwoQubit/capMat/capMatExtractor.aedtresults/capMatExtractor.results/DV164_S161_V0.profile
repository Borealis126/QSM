$begin 'Profile'
	$begin '56001'
		$begin 'ProfileGroup'
			MajorVer=2021
			MinorVer=1
			Name='Solution Process'
			StartInfo='Time:  05/14/2021 15:05:03; Host: c065; Processor: 36; OS: Linux 3.10.0-1160.15.2.el7.x86_64; Q3D 2021.1.0'
			TotalInfo='Elapsed time : 00:01:36 , ComEngine Memory : 98.1 M'
			GroupOptions=2
			TaskDataOptions(Memory=8)
			$begin 'ProfileGroup'
				MajorVer=2021
				MinorVer=1
				Name='Initialization'
				StartInfo='Time:  05/14/2021 15:05:03'
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
				StartInfo='Time:  05/14/2021 15:05:03'
				TotalInfo='Elapsed time : 00:00:03'
				GroupOptions=0
				TaskDataOptions(Memory=8)
				ProfileItem('  Mesh (phi surface)', 1, 0, 0, 0, 55328, 'I(1, 0, \'772 triangles\')', true, true)
			$end 'ProfileGroup'
			$begin 'ProfileGroup'
				MajorVer=2021
				MinorVer=1
				Name='Adaptive Meshing'
				StartInfo='Time:  05/14/2021 15:05:07'
				TotalInfo='Elapsed time : 00:01:33'
				GroupOptions=124
				TaskDataOptions()
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 1'
					StartInfo='Time:  05/14/2021 15:05:07'
					TotalInfo='Elapsed time : 00:00:04'
					GroupOptions=1182698032
					TaskDataOptions()
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c065 Using 16 core(s); 394664600 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 1, 0, 6, 0, 288396, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 1, 0, 288396, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 2'
					StartInfo='Time:  05/14/2021 15:05:11'
					TotalInfo='Elapsed time : 00:00:03'
					GroupOptions=1182698032
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 55520, 'I(1, 0, \'2142 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c065 Using 16 core(s); 394664600 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 0, 0, 7, 0, 451508, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 1, 0, 1, 0, 451508, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 3'
					StartInfo='Time:  05/14/2021 15:05:15'
					TotalInfo='Elapsed time : 00:00:04'
					GroupOptions=124
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 55544, 'I(1, 0, \'4630 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c065 Using 16 core(s); 394664600 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 1, 0, 13, 0, 639736, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 1, 0, 639736, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 4'
					StartInfo='Time:  05/14/2021 15:05:19'
					TotalInfo='Elapsed time : 00:00:04'
					GroupOptions=1182698032
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 55616, 'I(1, 0, \'9600 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c065 Using 16 core(s); 394664600 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 1, 0, 19, 0, 681556, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 1, 0, 5, 0, 681556, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 5'
					StartInfo='Time:  05/14/2021 15:05:24'
					TotalInfo='Elapsed time : 00:00:07'
					GroupOptions=1182698032
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 1, 0, 0, 0, 70400, 'I(1, 0, \'19852 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c065 Using 16 core(s); 394664600 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 2, 0, 34, 0, 931180, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 1, 0, 15, 0, 931180, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 6'
					StartInfo='Time:  05/14/2021 15:05:31'
					TotalInfo='Elapsed time : 00:00:11'
					GroupOptions=1182698032
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 1, 0, 1, 0, 109836, 'I(1, 0, \'39680 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c065 Using 16 core(s); 394664600 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 4, 0, 56, 0, 1010260, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 2, 0, 33, 0, 1083880, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 7'
					StartInfo='Time:  05/14/2021 15:05:42'
					TotalInfo='Elapsed time : 00:00:19'
					GroupOptions=1182698032
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 2, 0, 2, 0, 183316, 'I(1, 0, \'76762 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c065 Using 16 core(s); 394664600 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 7, 0, 84, 0, 1347640, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 6, 0, 84, 0, 1652824, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 8'
					StartInfo='Time:  05/14/2021 15:06:01'
					TotalInfo='Elapsed time : 00:00:38'
					GroupOptions=1182698032
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 4, 0, 4, 0, 315980, 'I(1, 0, \'143178 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c065 Using 16 core(s); 394664600 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 19, 0, 259, 0, 3070480, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 10, 0, 148, 0, 3499972, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				ProfileFootnote('I(1, 0, \'Adaptive Passes converged\')', 0)
			$end 'ProfileGroup'
			ProfileFootnote('I(1, 0, \'Time:  05/14/2021 15:06:40, Status: Normal Completion\')', 0)
		$end 'ProfileGroup'
	$end '56001'
$end 'Profile'
