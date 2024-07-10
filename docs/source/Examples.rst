Quickstart
################

A quick example how to learn a model on a given dataset.


.. code:: python

    # Import library
    import tafelvoetbal

    # Retrieve URLs of malicous and normal urls:
    X, y = tafelvoetbal.load_example()

    # Learn model on the data
    model = tafelvoetbal.fit_transform(X, y, pos_label='bad')

    # Plot the model performance
    results = tafelvoetbal.plot(model)



Learn new model with gridsearch and train-test set
################################################################

AAA

.. code:: python

    # Import library
    import tafelvoetbal

    # Load example data set    
    X,y_true = tafelvoetbal.load_example()

    # Retrieve URLs of malicous and normal urls:
    model = tafelvoetbal.fit_transform(X, y_true, pos_label='bad', train_test=True, gridsearch=True)

    # The test error will be shown
    results = tafelvoetbal.plot(model)


Learn new model on the entire data set
################################################

BBBB


.. code:: python

    # Import library
    import tafelvoetbal

    # Load example data set    
    X,y_true = tafelvoetbal.load_example()

    # Retrieve URLs of malicous and normal urls:
    model = tafelvoetbal.fit_transform(X, y_true, pos_label='bad', train_test=False, gridsearch=True)

    # The train error will be shown. Such results are heavily biased as the model also learned on this set of data
    results = tafelvoetbal.plot(model)


