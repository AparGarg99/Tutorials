################################################# LIBRARIES ##################################################
import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor
st.set_option('deprecation.showPyplotGlobalUse', False)

################################################# SIDEBAR ##################################################
st.sidebar.header('Specify Input Parameters')

def user_input_features():
    for i in var_names:
        globals()[i]= st.sidebar.slider(i, min(X[i]), max(X[i]), float(X[i].mean()))
    
    data = {'CRIM': CRIM,
            'ZN': ZN,
            'INDUS': INDUS,
            'CHAS': CHAS,
            'NOX': NOX,
            'RM': RM,
            'AGE': AGE,
            'DIS': DIS,
            'RAD': RAD,
            'TAX': TAX,
            'PTRATIO': PTRATIO,
            'B': B,
            'LSTAT': LSTAT}
    features = pd.DataFrame(data, index=[0])
    return features

############################################## BACKEND ML MODEL ################################################

boston = datasets.load_boston()
X = pd.DataFrame(boston.data, columns=boston.feature_names)
var_names = X.columns
Y = pd.DataFrame(boston.target, columns=["MEDV"])
# Build Regression Model
model = RandomForestRegressor()
model.fit(X, Y)
# Apply Model to Make Prediction
df = user_input_features()
prediction = model.predict(df)

# Explaining the model's predictions using SHAP values
# https://github.com/slundberg/shap
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

################################################# MAIN PAGE ##################################################

st.write("""
# Boston House Price Prediction App

This app predicts the **Boston House Price**!
""")
st.write('---')

# Print specified input parameters
st.header('Specified Input parameters')
st.write(df)
st.write('---')

st.header('Prediction of MEDV')
st.write(prediction)
st.write('---')

st.header('Feature Importance')

plt.title('Feature importance based on SHAP values')
shap.summary_plot(shap_values, X)
st.pyplot(bbox_inches='tight')
st.write('---')

plt.title('Feature importance based on SHAP values (Bar)')
shap.summary_plot(shap_values, X, plot_type="bar")
st.pyplot(bbox_inches='tight')
