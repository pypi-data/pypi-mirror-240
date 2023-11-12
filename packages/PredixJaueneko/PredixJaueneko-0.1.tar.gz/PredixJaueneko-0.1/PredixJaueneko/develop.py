from librerias import *

class ModeloOptimoExplicabilidad:
    def __init__(self, tabla, variable_objetivo, tipo_problema, test_size=0.2, random_state=33, mejor_modelo=False):
        self.tabla = tabla
        self.variable_objetivo = variable_objetivo
        self.tipo_problema = tipo_problema
        self.test_size = test_size
        self.random_state = random_state
        self.modelo_final = mejor_modelo
        self.xtrain = False
        self.xtest = False
        self.ytrain = False
        self.ytest = False

    def dividir_datos(self):
        try: 
            column_types = []
            for i in self.tabla.dtypes:
                column_types.append(i)
            column_types.pop(self.tabla.columns.get_loc(self.variable_objetivo))
            for dtype in column_types:
                if dtype == object:
                    raise ValueError()

            X_train, X_test, y_train, y_test = train_test_split(
                self.tabla.drop(self.variable_objetivo, axis=1),
                self.tabla[self.variable_objetivo],
                test_size=self.test_size,
                random_state=self.random_state
            )
            self.xtrain = X_train
            self.xtest = X_test
            self.ytrain = y_train
            self.ytest = y_test 
            return X_train, X_test, y_train, y_test
        except ValueError:
            print("El dataset ha de incluir valores numéricos")

    def evaluar_modelo(self, y_true, y_pred):
        if self.tipo_problema == 'regresion':
            mse = mean_squared_error(y_true, y_pred)
            r2 = r2_score(y_true, y_pred)
            return {'Mean Squared Error': mse, 'R-squared': r2}
        elif self.tipo_problema == 'clasificacion':
            accuracy = accuracy_score(y_true, y_pred)
            precision = precision_score(y_true, y_pred, average='weighted')
            recall = recall_score(y_true, y_pred, average='weighted')
            f1 = f1_score(y_true, y_pred, average='weighted')
            return {'Accuracy': accuracy, 'Precision': precision, 'Recall': recall, 'F1 Score': f1}


    def modelo_optimo(self):
        X_train, X_test, y_train, y_test = self.dividir_datos()

        if self.tipo_problema == 'regresion':
            modelos = [
                SVR(),
                RandomForestRegressor(),
                DecisionTreeRegressor()
            ]
        elif self.tipo_problema == 'clasificacion':
            modelos = [
                GradientBoostingClassifier(),
                RandomForestClassifier(),
                DecisionTreeClassifier()
            ]

        resultados = {}

        for modelo in modelos:
            modelo.fit(X_train, y_train)
            y_pred = modelo.predict(X_test)
            evaluacion = self.evaluar_modelo(y_test, y_pred)
            resultados[type(modelo).__name__] = evaluacion

        mejor_modelo = max(resultados, key=lambda k: resultados[k]['Accuracy'] if 'Accuracy' in resultados[k] else resultados[k]['R-squared'])
        self.modelo_final = mejor_modelo
        
        return f"El mejor modelo es {mejor_modelo} con métricas: {resultados[mejor_modelo]}"




class ModeloOptimoExplicabilidadConVariablesInfluyentes(ModeloOptimoExplicabilidad):
    def __init__(self, tabla, variable_objetivo, tipo_problema, k_variables, test_size=0.2, random_state=33, mejor_modelo=False):
        super().__init__(tabla, variable_objetivo, tipo_problema, test_size, random_state, mejor_modelo)
        self.k_variables = k_variables

    def obtener_variables_influyentes(self):
        X_train, X_test, y_train, y_test = self.dividir_datos()

        if self.tipo_problema == 'regresion':
            selector = SelectKBest(score_func=f_regression, k=self.k_variables)
        elif self.tipo_problema == 'clasificacion':
            selector = SelectKBest(score_func=f_classif, k=self.k_variables)

        selector.fit(X_train, y_train)
        variables_influyentes_indices = selector.get_support(indices=True)

        return variables_influyentes_indices

    def explicabilidad_shap(self, X_test):
        if not self.modelo_final:
            raise ValueError("No se ha ajustado ningún modelo todavía.")

        best_model = None

        if self.tipo_problema == 'regresion':
            if self.modelo_final == 'SVR':
                best_model = SVR()
            elif self.modelo_final == 'RandomForestRegressor':
                best_model = RandomForestRegressor()
            elif self.modelo_final == 'DecisionTreeRegressor':
                best_model = DecisionTreeRegressor()
        elif self.tipo_problema == 'clasificacion':
            if self.modelo_final == 'GradientBoostingClassifier':
                best_model = GradientBoostingClassifier()
            elif self.modelo_final == 'RandomForestClassifier':
                best_model = RandomForestClassifier()
            elif self.modelo_final == 'DecisionTreeClassifier':
                best_model = DecisionTreeClassifier()

        best_model.fit(self.xtrain,self.ytrain)

        # Crear una función que envuelva el modelo
        def model_predict(input_data):
            return best_model.predict(input_data)

        # Crear un objeto explainer de SHAP
        explainer = shap.Explainer(model_predict, self.xtrain)

        # Obtener las explicaciones SHAP para el conjunto de prueba
        shap_values = explainer(self.xtest)

        # Devolver las explicaciones SHAP
        return shap_values
