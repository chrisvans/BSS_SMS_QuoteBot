'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "AC38e4630890f311f112303c4f339e7dc8" 
AUTH_TOKEN = "15ed5af956d6f34279800e3f80852575"
BSSSPAM_APP_SID = "AP09101ffe4ee290094021b7c2509d588a"
BSS_SPAM_ID = "+16179817784"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
BSSSPAM_APP_SID = os.environ['BSSSPAM_APP_SID']
BSS_SPAM_ID = os.environ['BSS_SPAM_ID']
