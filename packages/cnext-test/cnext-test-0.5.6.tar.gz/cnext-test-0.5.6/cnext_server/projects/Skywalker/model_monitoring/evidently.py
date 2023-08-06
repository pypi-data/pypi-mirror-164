import pandas as pd
from sklearn import datasets
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab, CatTargetDriftTab
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection, CatTargetDriftProfileSection 
iris = datasets.load_iris()
iris_frame = pd.DataFrame(iris.data, columns = iris.feature_names)
iris_frame['target'] = iris.target
iris_target_drift_dashboard = Dashboard(tabs=[CatTargetDriftTab(verbose_level=1)])
iris_target_drift_dashboard.calculate(iris_frame[:75], iris_frame[75:], column_mapping=None)
iris_target_drift_dashboard.show(mode='inline')