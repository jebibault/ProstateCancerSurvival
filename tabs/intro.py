from dash.dependencies import Input, Output
from dash import dcc
from dash import html

from app import app

layout = [
html.P([html.Br()]),
html.P([html.Br()]),
dcc.Markdown("""
#### What is this model for?"""),
html.P([
	'In the United States alone, each year, an estimated 180,890 new cases will be diagnosed and 26,120 men will die from the disease. PSA testing has resulted in a significant increase in the diagnosis and treatment of prostate cancer. But the management of prostate cancer that is detected on the basis of prostate-specific antigen (PSA) levels remains controversial. ',
	html.Br(),
	html.Br(),
	'Many men do not benefit from treatment because the disease is either indolent or disseminated at diagnosis. Because prostate cancer progresses slowly, patients often die of competing causes.', 
	html.Br(),
	html.Br(),
	'We created this model to predict the risk to die from prostate cancer within 10 years after diagnosis.',
	html.Br(),
	html.Br(),
]),
dcc.Markdown("""
	#### The PLCO Trial
	The Prostate, Lung, Colorectal, and Ovarian (PLCO) Cancer Screening Trial was conducted
	to assess the role of prostate cancer screening on survival. From 1993 through 2001, 76,693 men at 10 
	U.S. study centers were randomized to receive either annual screening (38,343 subjects) or usual care as the control (38,350 subjects). 
	Men in the screening group were offered annual PSA testing for 6 years and digital rectal examination for 4 years. 
	The subjects and health care providers received the results and decided on the type of follow-up evaluation. 
	Results of the trial were published in three articles:"""),
	html.A("Andriole GL et al., New England Journal of Medicine, 2009", href='https://www.ncbi.nlm.nih.gov/pubmed/19297565', target="_blank", style={'font-weight': 'bold', 'color': '#820000', 'text-decoration': 'none'}),
	html.P([]),
	html.A("Andriole GL et al., Journal of the National Cancer Institute, 2012", href='https://www.ncbi.nlm.nih.gov/pubmed/22228146', target="_blank", style={'font-weight': 'bold', 'color': '#820000', 'text-decoration': 'none'}),
	html.P([]),
	html.A("Pinsky PF et al., Cancer, 2017", href='https://www.ncbi.nlm.nih.gov/pubmed/27911486', target="_blank", style={'font-weight': 'bold', 'color': '#820000', 'text-decoration': 'none'}),
	html.Br(),
	html.Br(),
	dcc.Markdown("""
	#### Data
	The data were obtained from the National Cancer Institute Cancer Data Access System:"""),
	html.A("National Cancer Institute Cancer Data Access System", href='https://cdas.cancer.gov/plco/', target="_blank", style={'font-weight': 'bold', 'color': '#820000', 'text-decoration': 'none'}),
	html.Br(),
	html.Br(),
	dcc.Markdown("""
	#### Model creation
	To build this model we selected the patients that were diagnosed with prostate cancer during follow-up (n=8,776). 
	The dataset was split into a training (n=7,021) and a testing (n=1,755) dataset.
	XGBoost was used to predict the risk to die from prostate cancer within 10 years after diagnosis. Hyperparameters were tuned with Bayesian Optimization in a nested cross-validation manner. Performances were evaluated on the test dataset with the bootstrap procedure."""),
	html.Br(),
	dcc.Markdown("""
	#### Model metrics:
	Evaluating models trained on unbalanced classes (the two classes we need to predict are not present in the dataset at the same ratio) can be difficult. We provide several methods to assess the performances of the model. All metrics are reported on the test dataset.

	|  Metric      |  Definition				 	                                                           |     PCa      |
	|--------------|-------------------------------------------------------------------------------------------|--------------|
	| Accuracy     |  Number of correct predictions / total number of input samples                            | 0.98 (±0.01) |
	| Precision    |  Number of correct positive predictions / number of positive predictions                  | 0.80 (±0.1)  |
	| Recall       |  Number of correct positive predictions / number of all positive samples                  | 0.60 (±0.08) |
	| f1-score     |  Harmonic mean of the precision and the recall                                            | 0.66 (±0.07) |
	| ROC AUC      |  Area under the curve of true positive rate and false positive rate at various thresholds | 0.80 (±0.04) |
	| PR AUC       |  Area under the curve of precision and recall at various thresholds                       | 0.54 (±0.07) |
	"""),
	html.Br(),
	html.Br(),
dcc.Markdown("""
### Disclaimer:
This application does not store any of the data provided for the predictions.
All information contained on this application is for general informational purposes only and does not constitute medical or other professional advice. It should not be used for medical purpose. The information you find on this application is provided as is and to the extent permitted by law, the creators disclaim all other warranties of any kind, whether express, implied, statutory or otherwise. In no event will the authors or its affiliates be liable for any damages whatsoever, including without limitation, direct, indirect, incidental, special, exemplary, punitive or consequential damages, arising out of the use, inability to use or the results of use of this application, any websites linked to this application or the materials or information or services contained at any or all such websites, whether based on warranty, contract, tort or any other legal theory and whether or not advised of the possibility of such damages. If your use of the materials, information or services from this application or any website linked to this application results in the need for servicing, repair or correction of equipment or data, you assume all costs thereof.""")
]




