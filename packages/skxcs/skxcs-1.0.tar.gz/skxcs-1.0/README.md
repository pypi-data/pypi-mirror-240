# skxcs

skxcs is a SciKit learn wrapper for implementation of XCS algorithm [xcs](https://github.com/hosford42/xcs). 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install skxcs. You need to have [Cython](https://pypi.org/project/Cython/) installed.

```bash
pip install skxcs
```

## Usage

Numeric Values

```python
from skxcs.classifiers import XcsClassifier
import pandas as pd
from sklearn.model_selection import train_test_split

# Numeric values
numerical_frame = pd.read_csv('https://raw.githubusercontent.com/kliegr/arcBench/master/data/datasets/iris.csv')
numerical_frame.dropna(inplace=True)
y = numerical_frame['class']
numerical_frame.drop('class', axis=1, inplace=True)
X_train, X_test, y_train, y_test = train_test_split(numerical_frame, y, test_size=0.33)

classifier = XcsClassifier()

# If data input is non binary, classifier automatically uses MLDP discretizer for numeric values
# and one hot encoding for categorical values to transform data in both fit and predict methods.

classifier.fit(X_train, y_train)

# Get prediction array
y_pred = classifier.predict(X_test)

# Get pretty rules
for rule in classifier.get_pretty_rules():
    print(rule)

# To use get_pretty_rules or pretty_print_prediction methods,
# classifier has to transform train and test data first.

```

Categorical values

```python
import pandas as pd
from skxcs.classifiers import XcsClassifier
from sklearn.model_selection import train_test_split

# Categorical values
categorical_frame = pd.read_csv('https://raw.githubusercontent.com/kliegr/arcBench/master/data/datasets/autos.csv')
categorical_frame.dropna(inplace=True)
y = categorical_frame['XClass']
categorical_frame = categorical_frame.select_dtypes(include=[object])
categorical_frame.drop('XClass', axis=1, inplace=True)
X_train, X_test, y_train, y_test = train_test_split(categorical_frame, y, test_size=0.25)
classifier = XcsClassifier()

# You can transform data yourself. You should either transform both training
# and testing data, or none of them. It is necessary to ensure correct values are passed to classifier.
X_train_bin = classifier.transform_df(X_train, y=y_train)
classifier.fit(X_train_bin, y_train)

# Note that we don't pass 'y' to transform method when we transform test data
X_test_bin = classifier.transform_df(X_test)

# pretty print prediction
result = classifier.pretty_print_prediction(X_test_bin)
print(result)
```

## Contributing
...

## License
[MIT](https://choosealicense.com/licenses/mit/)