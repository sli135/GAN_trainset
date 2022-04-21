{
 gROOT->Reset();

 gSystem->Load("libEXOUtilities");
 TChain t("tree");
 t.Add("/nfs/slac/g/exo_data2/exo_data/data/WIPP/root/5003/run00005003-000.root");
 //t.Add("/nfs/slac/g/exo_data4/exo_data/data/WIPP/root/5872/run00005872-000.root");
 EXOEventData* ed;
 t.SetBranchAddress("EventBranch",&ed);
 t->Draw("EventBranch.fEventHeader.fTriggerSource");
}