void SiPixelHistoricInfoPlotter() {
  char hisID[99]; 

  TFile *f = new TFile("/tmp/schuang/testPixelHistory.root", "READ"); 

  TH1F* errorType[15][40]; 
  for (int i=0; i<15; i++) {
    for (int j=0; j<40; j++) {
      sprintf(hisID,"errorType%d_%d",i+25,j); 
      errorType[i][j] = (TH1F*)f->Get(hisID)->Clone(); 
    }
  }
  TH1F* adc[20]; 
  TH1F* ndigis[20]; 
  TH1F* nclusters[20]; 
  TH1F* charge[20]; 
  TH1F* sizeX[20]; 
  TH1F* sizeY[20]; 
  TH1F* nRecHits[20]; 
  TH1F* residualX[20]; 
  TH1F* residualY[20]; 
  for (int i=0; i<20; i++) {
    sprintf(hisID,"adc_%d",100+i); 
    adc[i] = (TH1F*)f->Get(hisID)->Clone(); 

    sprintf(hisID,"nDigis_%d",100+i); 
    ndigis[i] = (TH1F*)f->Get(hisID)->Clone(); 

    sprintf(hisID,"nClusters_%d",100+i); 
    nclusters[i] = (TH1F*)f->Get(hisID)->Clone(); 

    sprintf(hisID,"charge_%d",100+i); 
    charge[i] = (TH1F*)f->Get(hisID)->Clone(); 

    sprintf(hisID,"clusterSizeX_%d",100+i); 
    sizeX[i] = (TH1F*)f->Get(hisID)->Clone(); 

    sprintf(hisID,"clusterSizeY_%d",100+i); 
    sizeY[i] = (TH1F*)f->Get(hisID)->Clone(); 
    /*
    sprintf(hisID,"nRecHits_%d",100+i); 
    nRecHits[i] = (TH1F*)f->Get(hisID)->Clone(); 

    sprintf(hisID,"residualX_%d",100+i); 
    residualX[i] = (TH1F*)f->Get(hisID)->Clone(); 

    sprintf(hisID,"residualY_%d",100+i); 
    residualY[i] = (TH1F*)f->Get(hisID)->Clone(); 
    */
  }
  TCanvas* cvs = new TCanvas("cvs","canvas for all drawings",1000,300);
  TPad* pd = new TPad("pd","pad for all drawings",0.01,0.01,0.99,0.99); 
        pd->Draw(); 

  gStyle->SetCanvasBorderMode(0);    
  gStyle->SetTitleBorderSize(0); 
  gStyle->SetTitleFontSize(0.06); 
  gStyle->SetPadLeftMargin(0.05);
  gStyle->SetPadRightMargin(0.05);
  gStyle->SetPadBottomMargin(0.12);
  gStyle->SetOptStat(0);       

  for (int i=0; i<15; i++) {
    for (int j=0; j<40; j++) {
      if (errorType[i][j]->Integral()>0.0) {
    	errorType[i][j]->SetMarkerStyle(8); 
    	errorType[i][j]->SetMarkerSize(0.4); 
    	errorType[i][j]->GetXaxis()->SetLabelSize(0.06); 
    	errorType[i][j]->Draw(); 
     	sprintf(hisID,"errorType%d_%d.gif",i+25,j);
    	cvs->SaveAs(hisID);  
      }
    }
  }
  for (int i=0; i<20; i++) { 
    adc[i]->SetMarkerStyle(8); 
    adc[i]->SetMarkerSize(0.4); 
    adc[i]->GetXaxis()->SetLabelSize(0.06); 
    adc[i]->Draw(); 
    sprintf(hisID,"adc_%d.gif",100+i); 
    cvs->SaveAs(hisID);  

    ndigis[i]->SetMarkerStyle(8); 
    ndigis[i]->SetMarkerSize(0.4); 
    ndigis[i]->GetXaxis()->SetLabelSize(0.06); 
    ndigis[i]->Draw(); 
    sprintf(hisID,"ndigis_%d.gif",100+i); 
    cvs->SaveAs(hisID);  

    nclusters[i]->SetMarkerStyle(8); 
    nclusters[i]->SetMarkerSize(0.4); 
    nclusters[i]->GetXaxis()->SetLabelSize(0.06); 
    nclusters[i]->Draw(); 
    sprintf(hisID,"nclusters_%d.gif",100+i); 
    cvs->SaveAs(hisID);  

    charge[i]->SetMarkerStyle(8); 
    charge[i]->SetMarkerSize(0.4); 
    charge[i]->GetXaxis()->SetLabelSize(0.06); 
    charge[i]->Draw(); 
    sprintf(hisID,"charge_%d.gif",100+i); 
    cvs->SaveAs(hisID);  

    sizeX[i]->SetMarkerStyle(8); 
    sizeX[i]->SetMarkerSize(0.4); 
    sizeX[i]->GetXaxis()->SetLabelSize(0.06); 
    sizeX[i]->Draw(); 
    sprintf(hisID,"clusterSizeX_%d.gif",100+i); 
    cvs->SaveAs(hisID);  

    sizeY[i]->SetMarkerStyle(8); 
    sizeY[i]->SetMarkerSize(0.4); 
    sizeY[i]->GetXaxis()->SetLabelSize(0.06); 
    sizeY[i]->Draw(); 
    sprintf(hisID,"clusterSizeY_%d.gif",100+i); 
    cvs->SaveAs(hisID);  
    /*
    nRecHits[i]->SetMarkerStyle(8); 
    nRecHits[i]->SetMarkerSize(0.4); 
    nRecHits[i]->GetXaxis()->SetLabelSize(0.06); 
    nRecHits[i]->Draw(); 
    sprintf(hisID,"nRecHits_%d.gif",100+i); 
    cvs->SaveAs(hisID);  

    residualX[i]->SetMarkerStyle(8); 
    residualX[i]->SetMarkerSize(0.4); 
    residualX[i]->GetXaxis()->SetLabelSize(0.06); 
    residualX[i]->Draw(); 
    sprintf(hisID,"residualX_%d.gif",100+i); 
    cvs->SaveAs(hisID);  

    residualY[i]->SetMarkerStyle(8); 
    residualY[i]->SetMarkerSize(0.4); 
    residualY[i]->GetXaxis()->SetLabelSize(0.06); 
    residualY[i]->Draw(); 
    sprintf(hisID,"residualY_%d.gif",100+i); 
    cvs->SaveAs(hisID);  
    */
  } 
} 
