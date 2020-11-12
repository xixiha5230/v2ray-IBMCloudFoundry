# IBMCloudFoundry

1. edit UUID and PATH in ``app.py``

2. run ``python app.py``

3. ``cd cloudfoundry``

4. edit name in ``manifest.yml``

5. deploy app to IBM cloud run:

   ``ibmcloud target --cf``  
   
   ``echo "N"|ibmcloud cf install ``
   
   ``ibmcloud cf push``
