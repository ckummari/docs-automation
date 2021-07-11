Terraform AWS documentation link
How to source code from innersource iac repositories in GitHub Actions ?
Terraform initialization step will source the code from private/internal repos using SSH Key.
Innersource iac repository SSH Key is added as an organization secret by default and should be passed in the Github Workflow.
Add the below code as a step in the workflow to install SSH Key in GitHub runner,

      - name: Install SSH Key
        run: |
          cd test
          mkdir ~/.ssh
          echo "${{ secrets.INNERSOURCE_IAC_KEY }}" >> ~/.ssh/id_rsa
          chmod 600 ~/.ssh/id_rsa