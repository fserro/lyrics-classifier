# pseudocode workflow

X = ['we all live in a yellow submarine', ... ]
y = ['Beatles', ...]

Xtrain, ... = train_test_split()

cv = CountVectorizer()

cv.fit(Xtrain)
Xtt = cv.transform(Xtrain)

m = LogisticRegression(C=0.01) # <-- regularize here
m.fit(Xtt, ytrain)
m.score(Xtt, ytrain)

cross_val_score(Xtt, ytrain)

Xtestt = cv.transform(Xtest)
m.score(Xtestt, ytest)

ypred = m.predict(Xtestt)        # ['Beatles', 'Eminem', ... ]

probs = m.predict_proba(Xtestt)  # array (N, 2)
pd.DataFrame(probs)

# prediction with user input
user = input()
user_t = cv.transform( [user] ) # <-- 1 data point
m.predict(user_t)

