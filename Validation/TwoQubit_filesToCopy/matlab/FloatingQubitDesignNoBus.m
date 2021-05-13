clear;close all
%%
%==================2 qubits coupled through bus resonator-V4=================
temp = importdata('FloatingQubitCapaMatNoBus_10MHz_gz - Copy.csv');
CapMat0 = temp.data;
CapMat0 = (CapMat0 + CapMat0')/2;

qubit_ind=[1 2];
reson_ind=[5 6];
wr=2*pi*[6.1e9 6.15e9];
Z0r=51.467514611130198*ones(size(wr));

phi_label=[1 1 2 2 0 0];
vect=[0,0];
%%
%============fix lumped part=======
Lq=11.5e-9*ones(size(qubit_ind));
Zq=zeros(size(qubit_ind));


Clr=pi./(2.*Z0r(1:length(reson_ind)).*wr(1:length(reson_ind)));
Llr=2*Z0r(1:length(reson_ind))./(pi*wr(1:length(reson_ind)));

fr0=1/2/pi./sqrt(Clr.*Llr);
Zlr=sqrt(Llr./Clr);

L_all=[Lq,Llr];
% Z_all=[Zq,Zlr];

CapMat=CapMat0;

for k=1:length(reson_ind)
    CapMat(reson_ind(k),reson_ind(k))=-sum(CapMat0(reson_ind(k),:))+abs(CapMat0(reson_ind(k),reson_ind(k)))+Clr(k);
end

%%
%============Gaussian elimination==========
NumOfFluxVar=length(phi_label);
ReducedReducedC = CapMat;
EliminatedRowsColumns = [];
IndTemp = [];
kk=1;
for k=1:floor(NumOfFluxVar/2)
    IndTemp=find(phi_label==k);
    if length(IndTemp)==2
        EliminatedRowsColumns=[EliminatedRowsColumns,IndTemp(1)];
        ChangeOfVar1 = eye(NumOfFluxVar);
        ChangeOfVar1(IndTemp(1), IndTemp(2)) = 1;
        ChangeOfVar1(IndTemp(2), IndTemp(2)) = -(-1)^vect(1, kk);
        ChangeOfVar2 = eye(NumOfFluxVar);
        ChangeOfVar2(IndTemp(2), IndTemp(1)) = (-1)^vect(kk)/2;
        ChangeOfVar3 = eye(NumOfFluxVar);
        ChangeOfVar3(IndTemp(2), IndTemp(2)) = 2;
        O_c=ChangeOfVar3*ChangeOfVar2*ChangeOfVar1;
        ReducedReducedC = ChangeOfVar1*ReducedReducedC*inv(ChangeOfVar3*ChangeOfVar2*ChangeOfVar1);
        GaussianColumnElimination = eye(NumOfFluxVar);
        GaussianColumnElimination(:,IndTemp(1)) = -ReducedReducedC(:, IndTemp(1))/ReducedReducedC(IndTemp(1), IndTemp(1));
        GaussianColumnElimination(IndTemp(1), IndTemp(1)) = 1;
        ReducedReducedC = GaussianColumnElimination*ReducedReducedC;
        kk=kk+1;
    end
end
ReducedC = ReducedReducedC;
for k=1:length(EliminatedRowsColumns)
    ReducedC(EliminatedRowsColumns(k)-k+1,:)=[];
    ReducedC(:,EliminatedRowsColumns(k)-k+1)=[];
end
ReducedC;
% for k1=1:length(ReducedC)
%      ReducedC(k1,k1)=ReducedC(k1,k1)-abs(ReducedC(end,k1));
% end
% % ReducedC(:,end)=[];
% % ReducedC(end,:)=[];
[m,n]=size(ReducedC);
diagm=diag(ones(1,m));
%Sign_fix=2*(diagm-0.5);
%C_1=abs(ReducedC).*Sign_fix;

C_2=ReducedC;



InvC=inv(C_2);
C_prim_all=1./transpose(diag(InvC));
Z_all=sqrt(L_all./C_prim_all);

InvImped=kron(transpose(1./sqrt(2*Z_all)),1./sqrt(2*Z_all));

Plasama_circuit=InvC.*InvImped;

n=size(Plasama_circuit,1);

Plasama_circuit(1:(n+1):end)=Plasama_circuit(1:(n+1):end)*2;
Plasama_circuit=Plasama_circuit/2/pi/1e9;

Ec = zeros(1,length(C_prim_all));
Alpha = zeros(1,length(C_prim_all));

QuantizedCircuit = Plasama_circuit;
e_const = 1.60217662e-19;
h_const = 6.62607004e-34;


for ii=qubit_ind
    Ec(ii) = e_const^2/(2*C_prim_all(ii))/h_const/1e9;
    QuantizedCircuit(ii,ii) = Plasama_circuit(ii,ii) - Ec(ii)/(1-(Ec(ii)/Plasama_circuit(ii,ii)));
    Alpha(ii) = - Ec(ii)*(Plasama_circuit(ii,ii)/QuantizedCircuit(ii,ii))^2;
end

chi = zeros(size(QuantizedCircuit));
chi_old = zeros(size(QuantizedCircuit));
Resonator_shift = zeros(size(QuantizedCircuit));
for ii = qubit_ind
    for jj = reson_ind - sum(phi_label~=0)/2
        chi(ii,jj) = 4*Alpha(ii)*(QuantizedCircuit(ii,jj)*QuantizedCircuit(jj,jj)/(QuantizedCircuit(jj,jj)^2-QuantizedCircuit(ii,ii)^2))^2;
        chi(jj,ii) = chi(ii,jj);
        Resonator_shift(ii,jj) = QuantizedCircuit(ii,jj)^2/(QuantizedCircuit(jj,jj)-QuantizedCircuit(ii,ii));
        Resonator_shift(jj,ii) = Resonator_shift(ii,jj);
        chi_old(ii,jj) = QuantizedCircuit(ii,jj)^2*abs(Alpha(ii))/(abs(Alpha(ii))+QuantizedCircuit(jj,jj)-QuantizedCircuit(ii,ii))/(QuantizedCircuit(jj,jj)-QuantizedCircuit(ii,ii));
        chi_old(jj,ii) = Resonator_shift(ii,jj);
    end
end

QuantizedCircuit;
Alpha;
Ec;
%Resonator_shift
chi;
chi_old;

%%
%================calculate two qubit spectrum================
omega_q1 = QuantizedCircuit(1,1);
omega_q2 = QuantizedCircuit(2,2);
omega_readout1 = QuantizedCircuit(3,3);
omega_readout2 = QuantizedCircuit(4,4);

g_q1_q2 =  QuantizedCircuit(1,2); %in GHz
alpha1 = abs(Alpha(1));
alpha2 = abs(Alpha(2));


g_1001 = g_q1_q2;

g_2011 = sqrt(2)*sqrt(1)*g_q1_q2;
g_1102 = sqrt(1)*sqrt(2)*g_q1_q2;;

g_3021 = sqrt(3)*sqrt(1)*g_q1_q2;;
g_2112 = sqrt(2)*sqrt(2)*g_q1_q2;;
g_1203 = sqrt(1)*sqrt(3)*g_q1_q2;;

H1 = [omega_q1,     g_1001;...
	g_1001,         omega_q2];

H2 = [2*omega_q1 - alpha1,       g_2011,                0;...
	g_2011,         omega_q1+omega_q2,       g_1102;...
	0,                  g_1102,         2*omega_q2 - alpha2];

H3 = [3*omega_q1 - 3*alpha1,                g_3021,                                0,                      0;...
	g_3021,               2*omega_q1 - alpha1 + omega_q2,            g_2112,                        0;...
	0,                                g_2112,                omega_q1+2*omega_q2-alpha2,           g_1203;...
	0,                                   0,                           g_1203,                3*omega_q2 - 3*alpha2];
H_tot = blkdiag(0,H1,H2,H3);
[EigenVectors,EigenValuesMatrix] = eig(H_tot);
Energy_levels = diag(EigenValuesMatrix);
[Energy_levels, ind_el] = sort(Energy_levels);
EigenVectors = EigenVectors(:,ind_el);
Energy_levels_uncoupled = [0; diag(H1); diag(H2); diag(H3)];
[~,ind_sorted] = ismember(Energy_levels_uncoupled, sort(Energy_levels_uncoupled));

%%
E00 = 0;
Psi00 = zeros(10,length(omega_q1));
Psi00(1) = 1;
% one excitation manifold

E10 = Energy_levels(ind_sorted(2));
E01 = Energy_levels(ind_sorted(3));

Psi10 = EigenVectors(:,ind_sorted(2));
Psi01 = EigenVectors(:,ind_sorted(3));

%%
% two excitation manifold
E20 = Energy_levels(ind_sorted(4));
E11 = Energy_levels(ind_sorted(5));
E02 = Energy_levels(ind_sorted(6));

Psi20 = EigenVectors(:,ind_sorted(4));
Psi11 = EigenVectors(:,ind_sorted(5));
Psi02 = EigenVectors(:,ind_sorted(6));

%%
% three excitation manifold
E30 = Energy_levels(ind_sorted(7));
E21 = Energy_levels(ind_sorted(8));
E12 = Energy_levels(ind_sorted(9));
E03 = Energy_levels(ind_sorted(10));

Psi30 = EigenVectors(:,ind_sorted(7));
Psi21 = EigenVectors(:,ind_sorted(8));
Psi12 = EigenVectors(:,ind_sorted(9));
Psi03 = EigenVectors(:,ind_sorted(10));

%%
% some transition frequencies
omega_1121 = E21 - E11;
omega_1020 = E20 - E10;
omega_1011 = E11 - E10;
omega_1112 = E12 - E11;
omega_0102 = E02 - E01;



xshift_unit = omega_q2*0.7;


Dipole_transition_Matrix = zeros(10);

sigma_x_q1 = diag(sqrt(1:3)./[omega_readout1 - omega_q1+(0:2)*alpha1],-1) + diag(sqrt(1:3)./[omega_readout1 - omega_q1+(0:2)*alpha1],1);
sigma_x_q2 = diag(sqrt(1:3)./[omega_readout2 - omega_q2+(0:2)*alpha1],-1) + diag(sqrt(1:3)./[omega_readout2 - omega_q2+(0:2)*alpha1],1);

Dipole_original = kron(sigma_x_q1,eye(4)) - kron(eye(4),sigma_x_q2);
Dipole_original([8 11 12 14 15 16],:) = [];
Dipole_original(:,[8 11 12 14 15 16]) = [];



E_original = [1 3 6 10 2 5 9 4 8 7]';
[~,indx_levels] = sortrows(E_original);

temp = Dipole_original(indx_levels,:);
temp = transpose(temp);
Dipole_transition_Matrix = transpose(temp(indx_levels,:));

% level_label = cell(1,10);
SinglePhoton_Transition = cell(1,1);
SinglePhoton_freq = [];
SinglePhoton_matrix_element = [];
ks=0;
TwoPhoton_Transition = cell(1,1);
TwoPhoton_freq = [];
TwoPhoton_matrix_element = [];
kt=0;
figure
hold on
for nn = 0:3
    for mm = 0:nn
        if nn~=0 | mm~=0
            eval(['temp_state_coeff = transpose(Psi',num2str(nn-mm),num2str(mm),');']);
            temp_state_coeff(temp_state_coeff==0) = [];
            state_coeff_strings = num2str(temp_state_coeff,'%10.2e,');
            state_coeff_strings(end) = [];
            state_coeff_strings = ['(',state_coeff_strings,')'];
        end
        
        if nn<3
            for one_excited_level_ind = 0:nn+1
            ks = ks + 1;
            SinglePhoton_Transition{ks,1} = ['f_',num2str(nn-mm),num2str(mm),'_',num2str(nn-one_excited_level_ind+1),num2str(one_excited_level_ind)];
            eval(['SinglePhoton_freq(ks,1) = E',num2str(nn-one_excited_level_ind+1),num2str(one_excited_level_ind),'-E',num2str(nn-mm),num2str(mm),';']);
			eval(['SinglePhoton_matrix_element(ks,1) = Psi',num2str(nn-one_excited_level_ind+1),num2str(one_excited_level_ind),'''*Dipole_transition_Matrix*Psi',num2str(nn-mm),num2str(mm),';']);
            end
        end
        if nn<2
			for two_excited_level_ind = 0:nn+2
            kt = kt + 1;
            TwoPhoton_Transition{kt,1} = ['f_',num2str(nn-mm),num2str(mm),'_',num2str(nn-two_excited_level_ind+2),num2str(two_excited_level_ind)];
            eval(['TwoPhoton_freq(kt,1) = (E',num2str(nn-two_excited_level_ind+2),num2str(two_excited_level_ind),'-E',num2str(nn-mm),num2str(mm),')/2;']);
			temp = 0;
			for one_excited_level_ind = 0:nn+1
				eval(['temp = temp + (Psi',num2str(nn-two_excited_level_ind+2),num2str(two_excited_level_ind),'''*Dipole_transition_Matrix*Psi',num2str(nn-one_excited_level_ind+1),num2str(one_excited_level_ind),')*(Psi',num2str(nn-one_excited_level_ind+1),num2str(one_excited_level_ind),'''*Dipole_transition_Matrix*Psi',num2str(nn-mm),num2str(mm),');']);
			end
			TwoPhoton_matrix_element(kt,1) = temp;
			end
        end
        %        level_label{nn*(nn+1)/2+mm+1} = [num2str(nn-mm),num2str(mm)];
        % plot(linspace(-xshift_unit/2,xshift_unit/2,100)-xshift_unit*(nn-mm)+xshift_unit*mm,E01*ones(1,100),'r-','linewidth',5)
        eval(['plot(linspace(-xshift_unit/2,xshift_unit/2,100)-xshift_unit*(nn-mm)+xshift_unit*mm,E',num2str(nn-mm),num2str(mm),'*ones(1,100),''r-'',''linewidth'',4)']);
        eval(['text(-xshift_unit*(nn-mm+0.35)+xshift_unit*mm,E',num2str(nn-mm),num2str(mm),'-omega_q2/6,''|',num2str(nn-mm),num2str(mm),'> =',eval(['num2str(E',num2str(nn-mm),num2str(mm),')']),' GHz'',''Color'',''black'',''FontSize'',12)'])
        if nn~=0 | mm~=0
%             eval(['text(-xshift_unit*(nn-mm+0.7)+xshift_unit*mm,E',num2str(nn-mm),num2str(mm),'-omega_q2/3,',state_coeff_strings,',''Color'',''black'',''FontSize'',12)'])
            eval(['text(-xshift_unit*(nn-mm+',num2str(0.2*(nn+1)),')+xshift_unit*mm,E',num2str(nn-mm),num2str(mm),'+omega_q2/6,state_coeff_strings,''Color'',''black'',''FontSize'',12)'])
        end
    end
end
hold off
% axis equal
ax1 = gca;
ax1.Visible = 'off'; % remove x-axis
set(gcf,'color', [1 1 1]);
ScreenSize = get(0,'ScreenSize');
PlotSize = [ScreenSize(3)*0.05 ScreenSize(4)*0.1 ScreenSize(3)*0.85 ScreenSize(4)*0.8];
set(gcf,'position',PlotSize)

Transition_type_single_photon = ones(size(SinglePhoton_freq));
Transition_type_two_photon = 2*ones(size(TwoPhoton_freq));

Transition_type = [Transition_type_single_photon; Transition_type_two_photon];
Transition = [SinglePhoton_Transition; TwoPhoton_Transition];
Transition_freq = [SinglePhoton_freq; TwoPhoton_freq];
SinglePhoton_matrix_element_normalized = abs(SinglePhoton_matrix_element)/max(abs(SinglePhoton_matrix_element));
TwoPhoton_matrix_element_normalized = abs(TwoPhoton_matrix_element)/max(abs(TwoPhoton_matrix_element));
Matrix_element_normalized = [SinglePhoton_matrix_element_normalized; TwoPhoton_matrix_element_normalized];

%tblTransition = table(Transition, Transition_type, Transition_freq, Matrix_element_normalized)
%tblTransition = sortrows(tblTransition,3)
%%
%figure
%hold on
%for is = 1:length(SinglePhoton_freq)
%    plot(ones(1,10)*SinglePhoton_freq(is),linspace(0,SinglePhoton_matrix_element_normalized(is),10),'b-', 'linewidth',2)
%end
%for it = 1:length(TwoPhoton_freq)
%    plot(ones(1,10)*TwoPhoton_freq(it),linspace(0,TwoPhoton_matrix_element_normalized(it),10),'r-', 'linewidth',2)
%end
%hold off
%axis([floor(min(Transition_freq)) ceil(max(Transition_freq)) 0 1.2])
% figure
% yyaxis left
% plot((omega_q1-omega_q2)/alpha,omega_1121,'r-')
% hold on
% plot((omega_q1-omega_q2)/alpha,omega_1020,'b-')
% plot((omega_q1-omega_q2)/alpha,omega_1011,'m-')
Dipole_ratio_q1 = SinglePhoton_matrix_element_normalized(7)/SinglePhoton_matrix_element_normalized(1);
Dipole_ratio_q2 = SinglePhoton_matrix_element_normalized(4)/SinglePhoton_matrix_element_normalized(2);
deltaI = (E11 - E01) - (E10 - E00);
deltaO = (E12 - E11) - (E02 - E01);
Dipole_ratio_O_q2 = SinglePhoton_matrix_element_normalized(8)/SinglePhoton_matrix_element_normalized(15);