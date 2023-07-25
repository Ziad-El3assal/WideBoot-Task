## Firstly I go for Preprocessing :
  1) Data Normalization: This is just to make sure all characters appear in the same in all the text.
  2) Remove Diacritics: Diacritics are small marks that modify the pronunciation of letters. Removing diacritics can help reduce the complexity of the text and standardize it for processing.
  3) Stepwords Removal: Remove common words that do not carry significant meaning (e.g., articles, prepositions, conjunctions). Create a list of Arabic stop words and eliminate them from the text.
## The Modeling
<heading>Text Classification using XGBoost and TF-IDF</heading>

<paragraph>
  This project demonstrates a text classification task using the XGBoost algorithm with TF-IDF (Term Frequency-Inverse Document Frequency) features.
</paragraph>

<steps>
  <step number="1">Data Preparation:</step>
  <content>
    <paragraph>
      The data is assumed to be in a DataFrame called 'data' with columns 'title', 'story', and 'topic'. The 'title' and 'story' columns are combined into a new column called 'combined_text', which concatenates the text from both columns.
    </paragraph>
  </content>
  
  <step number="2">Data Shuffling:</step>
  <content>
    <paragraph>
      The data is shuffled to ensure randomness using the 'sample' function with 'frac=1' and 'random_state=42'.
    </paragraph>
  </content>
  
  <step number="3">Stratified Sampling for Test Set:</step>
  <content>
    <paragraph>
      The data is split into training and testing sets using 'train_test_split'. 20% of the data is reserved as the test set while preserving the class distribution with 'stratify=y'.
    </paragraph>
  </content>
  
  <step number="4">Text Vectorization with TF-IDF:</step>
  <content>
    <paragraph>
      The text data is converted into numerical feature vectors using 'TfidfVectorizer' from scikit-learn. It transforms the text data into a sparse matrix of TF-IDF features.
    </paragraph>
  </content>
  
  <step number="5">XGBoost Model Creation and Training:</step>
  <content>
    <paragraph>
      An XGBoost classifier is created and trained on the TF-IDF transformed training data using 'xgb.XGBClassifier'.
    </paragraph>
  </content>
  
  <step number="6">Model Evaluation:</step>
  <content>
    <paragraph>
      The trained XGBoost classifier is used to predict labels for the test set. The accuracy of the model is calculated using 'accuracy_score' to compare the predicted labels with the true labels.
    </paragraph>
  </content>
</steps>

<conclusion>
  <paragraph>
    The combination of XGBoost and TF-IDF provides a powerful solution for text classification tasks, enabling the model to predict topic labels with high accuracy and efficiency.
  </paragraph>
</conclusion>
