name: GenerateEnsemble

on:

  workflow_dispatch:

  workflow_run:
    workflows: [GenerateBaseline]
      
    types:
      - completed


jobs:
  
  ensemble_job:
    if: ${{ github.event.workflow_run.conclusion == 'success' && github.repository_owner == 'Testing-Forecast-Actions' }}
    runs-on: ubuntu-latest

    steps:
    
    - name: test only step
      run: ehco "Gira ensemble"
