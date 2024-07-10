
Save and Load
''''''''''''''

Saving and loading models is desired as the learning proces of a model for ``tafelvoetbal`` can take up to hours.
In order to accomplish this, we created two functions: function :func:`tafelvoetbal.save` and function :func:`tafelvoetbal.load`
Below we illustrate how to save and load models.


Saving
----------------

Saving a learned model can be done using the function :func:`tafelvoetbal.save`:

.. code:: python

    import tafelvoetbal

    # Load example data
    X,y_true = tafelvoetbal.load_example()

    # Learn model
    model = tafelvoetbal.fit_transform(X, y_true, pos_label='bad')

    Save model
    status = tafelvoetbal.save(model, 'learned_model_v1')



Loading
----------------------

Loading a learned model can be done using the function :func:`tafelvoetbal.load`:

.. code:: python

    import tafelvoetbal

    # Load model
    model = tafelvoetbal.load(model, 'learned_model_v1')

