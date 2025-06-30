name: GenerateEnsemble

on:

  workflow_dispatch:

  workflow_run:
    workflows: [PersistChangesToJsonDB]
      
    types:
      - completed
    
jobs:
  
  verify_ensemble_job:
    if: ${{ github.event.workflow_run.conclusion == 'success' && github.repository_owner == 'Testing-Forecast-Actions' }}
    runs-on: ubuntu-latest
    outputs: 
      baseline_exists: ${{ steps.check_baseline.outputs.bl_exists == 'exists' }}

    steps:
      
    # Checkout the python tools repo
    # -------------------------------------------      
    - name: checkout python tools repo
      uses: actions/checkout@v3
      with:
        token: ${{ secrets.GITHUB_TOKEN }}
        repository: 'Testing-Forecast-Actions/Testing-Tools'
        ref: 'main'
        path: './tools/'

    # Checkout the data repository
    # -------------------------------------------      
    - name: checkout data repo
      uses: actions/checkout@v3
      with:
        token: ${{ secrets.GITHUB_TOKEN }}
        repository: 'Testing-Forecast-Actions/RespiCast-SyndromicIndicators'
        ref: 'main'
        path: './repo/'



    # Run Pyton code
    # -------------------------
    - uses: actions/setup-python@v4
      with:
        python-version: '3.10' 

    # Verify if baseline already exists
    # this will write "exists" or "missing" in the out var baseline_exists
    - name: check baseline exists
      id: check_baseline
      run: |
        python ./tools/code/FH_current_baseline_exists.py --hub_path ./repo
