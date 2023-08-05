Procuring access credentials
============================

To initialize a connection to a cloud and get a provider object, you will need
to provide the cloud's access credentials to CloudBridge. This page will walk
you through the process of procuring credentials on different providers. For
more information on using the obtained credentials with CloudBridge, see
`Connection and Authentication Setup <setup.html>`_ page.

.. _azure-creds:

Microsoft Azure
---------------

The page linked below from the Microsoft documentation was used to create this
section, and can be followed instead of this CloudBridge-specific documentation
to procure Azure credentials
https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal.

In order to follow the instructions below, one needs a Microsoft Azure account
and an active Subscription, as well as web portal access:
https://portal.azure.com/ The following section will walk you through the
process of creating an application, which is required for API access, as well
as help you locate all required Azure credentials for API access via
CloudBridge.

Azure credentials require a `Subscription ID` which can be procured through
`Subscriptions` in the Azure portal.

.. figure:: captures/az-sub-1.png
   :alt: Azure Subscriptions 1

   Subscriptions can be accessed by searching, or by choosing `Subscriptions`
   in the `All Services` window

.. figure:: captures/az-sub-2.png
   :alt: Azure Subscriptions 2

   The `Subscription ID` will be found in the list of subscriptions


Another piece of credentials that already exists on any Azure account is a
`Tenant ID` which will correspond to the `Active Directory ID`, which can be
procured through the Azure Active Directory's `Properties`.

.. figure:: captures/az-dir-1.png
   :alt: Azure Directory 1

   The `Azure Active Directory` can be access by searching, or by choosing
   `Azure Active Directory` in the `All Services` window.
   `Azure Active Directory` is also a default favorite on the sidebar.

.. figure:: captures/az-dir-2.png
   :alt: Azure Directory 2

   The `Directory ID` will be found in the Directory's `Properties` section


In order to access the API, an application needs to be registered and a key
needs to be created. After creating an application through the
`App Registrations` window under the `Active Directory`, the `Application ID`
of the app will correspond to the `Client ID` in CloudBridge, and the
generated value of its key, will correspond to the `Secret`.


.. figure:: captures/az-app-1.png
   :alt: Azure App 1

   `App Registrations` can be access by searching, or through choosing
   `App Registrations` under `Azure Active Directory`.

.. figure:: captures/az-app-2.png
   :alt: Azure App 2

   The `New Application Registration` button will allow users to create a
   new application

.. figure:: captures/az-app-3.png
   :alt: Azure App 3

   The `Name` has to be unique within the subscription and will be used to
   identify the `Application` later on. The `Sign-on URL` can be any
   URL-looking string. It does not have to point towards anything.

.. figure:: captures/az-app-4.png
   :alt: Azure App 4

   After creating the application, one must select it, after which the
   `Application ID` will map to the `Client ID` in CloudBridge.

.. figure:: captures/az-app-5.png
   :alt: Azure App 5

   In the application's `Settings` panel, under the `Keys` section, one will
   be able to create a new `Secret`.

.. figure:: captures/az-app-6.png
   :alt: Azure App 6

   Any name can be given to the key, and any expiration date, after which
   the `Save` button will generate the `Key` which will correspond to the
   `Secret` in CloudBridge.

.. figure:: captures/az-app-7.png
   :alt: Azure App 7

   The value of the key will correspond to the `Secret` in CloudBridge and
   needs to be saved at creation-time.


Finally, in order to have appropriate permissions, you must assign an
appropriate role to the newly created application. Permissions can be
assigned at the level of the Subscription, or at the level of each Resource
Group. `Contributor` access is recommended for general use in order to have
sufficient permissions to create and manage all types of resources, but
specific roles can also be assigned for more limited access.


.. figure:: captures/az-role-1.png
   :alt: Azure Roles 1

   Subscription-level access will allow the application to access resources
   from multiple resource groups.

.. figure:: captures/az-role-2.png
   :alt: Azure Roles 2

   When roles are set at the level of the Resource Group, one must specify
   this Resource Group as part of the credentials, as the application will
   not have enough permissions to create a Resource Group.

.. figure:: captures/az-role-3.png
   :alt: Azure Roles 3

   Adding a role assignment to the application will give it appropriate
   permissions to manage resources.

.. _google-creds:

Google Cloud Platform (GCP)
---------------------------

For Google Cloud Platform (GCP), create a service account followed by creating
and downloading a key. Additional instructions are available at this link
https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating_a_service_account.

Start off by clicking on the `Create Service Account` button on the
IAM & admin section of the Google Cloud Console:
https://console.cloud.google.com/iam-admin/serviceaccounts.

.. figure:: captures/gcp-sa-1.png
   :alt: GCP Service Account 1

Next, we provide a name for the service account and an informative description.
Note that the supplied name is used to create an email address for the service
account. Once created, this email cannot be changed.

.. figure:: captures/gcp-sa-2.png
   :alt: GCP Service Account 2

We then assign a role to the service account. Depending on what you will be
doing with the service account, and CloudBridge, you can set granular access
roles for the service account. The `Editor` role on the project is very broad
and will allow you to exercise all of the CloudBridge capabilities.

.. figure:: captures/gcp-sa-3.png
   :alt: GCP Service Account 3

After a service account has been created, we need to add a key to it.

.. figure:: captures/gcp-sa-4.png
   :alt: GCP Service Account key 1

Finally, choose the JSON format for the key when prompted. The file that is
downloaded will be used with CloudBridge through the variables shown
on the `Connection and Authentication Setup <setup.html>`_ page. Note that you
may have multiple keys associated with the same service account.

.. figure:: captures/gcp-sa-5.png
   :alt: GCP Service Account key 2

The JSON credentials file will have a similar form to the example shown
below, and can either be passed through an absolute path to the file, or
through a variable containing the JSON dictionary itself.


.. code-block:: json

    {
      "type": "service_account",
      "project_id": "my-project",
      "private_key_id": "b12321312441245gerg245245g42c245g254t425",
      "private_key": "-----BEGIN PRIVATE KEY-----\nMIICWgIBAAKBgE1EJDPKM/2wck/CZYCS7F2cXoHXDBhXYtdeV+h70Nk+ABs6scAV\nApYoobJAVpDeL+lutYAwtbscNz5K915DiNEkBf48LhfBWc5ea07OnClOGC9zASja\nif6ujIdhbITaNat9rdG939gQWqyaDW4wzYfvurhfmxICNgZA1YpWco1HAgMBAAEC\ngYAc+vLtLelEPNsTSWGS0Qiwr8bOwl75/kTHbM5iF5ak9NlLXT9wQTEgKwtC9VjC\nq2OjFXAkLaDsFlAuICYaCBCXn1nUqNoYhaSEQNwGnWIz376letXg/mX+BALSPMFR\nhE6mbdmaL4OV1X8j8uf2VcrLfVFCCZfhPu/TM5D6bVFYoQJBAJRHNKYU/csAB/NE\nzScJBv7PltOAoYpxbyFZb1rWcV9mAn34382b0YBXbp3Giqvifs/teudUbRpAzzLm\n5gr8tzECQQCFZh4tNIzeZZYUqkQxrxgqnnONey1hX7K+BlGyC6n2o26sE+I7cLij\n2kbuWoSFMAIdM2Hextv9k+ZrwUas4V33AkAfi9Korvib0sLeP7oB3wrM9W9aShiU\nMrP4/WUSh2MRb8uB74v123vD+VYAXTgtf3+JTzYBt1WK61TpuHQizEdRAkBjt8hL\nBoNfJBUicXz0nuyzvyql0jREG+NjhRnAvFNbGSR74Yk14bdEVMC9IFD7tr190pEQ\nlRqR3eNbHWmVhgpVAkBgveeM73R1tFXS6UosBtfDI1zut44Ce0RoADOIxjXqgjOi\nXSrevYvoKCl09yhLNAnKD+QvT/YbshW/jibYXwdj\n-----END PRIVATE KEY-----",
      "client_email": "service-name@my-project.iam.gserviceaccount.com",
      "client_id": "13451345134513451345",
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://oauth2.googleapis.com/token",
      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
      "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/service-name%40my-project.iam.gserviceaccount.com"
    }

To pass in the values as a properly escaped multi-line environment variable, use
the following:

.. code-block:: shell

    export GCP_SERVICE_CREDS_DICT=`cat ~/path/to/gcp-creds.json`


.. Comments for documentation authors:
.. When uploading pictures, process them using sips, as follows:
.. sips -s format png -Z 1500 img-name.png
