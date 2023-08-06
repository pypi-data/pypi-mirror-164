function readfrc()
% This function is used to read and plot the residuals of FD forces
% following the directory hierarchy of RESCUPy's fdforces.py module as of
% commit 702b9fa2cc635657eb350a19e319f93328a44d9b.
root=pwd;
figure()
set(0,'DefaultLineLineWidth',2)
d = dir('frc_res*');
fref = cell(numel(d),1);
for i = numel(d):-1:1
   cd(root)
   cd(d(i).name)
   [hs,fref{i}] = readfrc1();
end
res = zeros(numel(d)-1,1);
for i = numel(d):-1:2
   tmp = fref{i}-fref{1};
   res(i) = norm(tmp(:),'inf');
   dname = regexprep(d(i).name, '[\\\^\_]','\\$0');
   loglog(hs,res(i)*ones(size(hs)),'--', 'DisplayName', dname)
end
xlabel('h (ang)')
ylabel('max(F_{err}) (eV/ang)')
title('Residual wrt HF (at given resolution)')
legend('Location','NorthWest')
cd(root)

function [hs,fref] = readfrc1()

root=pwd;
fprintf('%s\n', root);
d = dir('frc*');
hs = zeros(numel(d),1);
res = zeros(numel(d),1);
for i = 1:numel(d)
   if ~d(i).isdir; continue; end
   cd(root)
   cd(d(i).name)
   [frc, fref, h, r] = readfrc2();
   fprintf('h = %1.3e\n', h);
   hs(i) = h;
   res(i) = r;
   printarr(frc)
end
fprintf('HF\n');
printarr(fref)
[~,dname]=fileparts(root);
dname = regexprep(dname, '[\\\^\_]','\\$0');
loglog(hs,res,'-o','DisplayName',dname); hold on
cd(root)

function printarr(frc)
fprintf('[\n');
for j = 1:size(frc,1)
   fprintf('[%f %f %f];\n', frc(j,:));
end
fprintf(']\n');

function [frc, fref, h, res] = readfrc2()

root=pwd;
d = dir('etot_*');
etots = zeros(numel(d),1);
load('etot_center/results/scf.mat','atom','energy', 'force')
fld = 'Ftot';
fref = force.total;
etots(1) = energy.(fld);
x0 = atom.xyz(1);
d = dir('etot_atm*');
natm = numel(d)/3;
frc = zeros(natm, 3);
for i = 1:numel(d)
   if ~d(i).isdir; continue; end
   cd(root)
   cd(d(i).name)
   load('results/scf.mat','atom','energy')
   x1 = atom.xyz(1);
   if i == 1
      h = x1 - x0;
   end
   etots(i+1) = energy.(fld);
end
frc = -(reshape(etots(2:end),[],2)' - etots(1)) / h;
BOHR2ANG = 0.52917721067; HA2EV = 27.21138602;
h = h * BOHR2ANG;
frc = frc / BOHR2ANG * HA2EV;
fref = fref / BOHR2ANG * HA2EV;
res = frc - fref;
res = norm(res(:),'inf');
cd(root)


