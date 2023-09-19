name: CI
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: install packages
        run: make install
      - name: lint
        run: make lint
      - name: test
        run: make test
      - name: format
        run: make format
      - name: deploy
        run: make deploy 
      - name: Run main script
        run: python main.py
      - name: List files
        run: |
          pwd
          ls -R  

      - name: Archive and Upload Artifacts
        uses: actions/upload-artifact@v3
        with:
          name: ml_pipeline-artifacts
          path: ${{ github.workspace }}/output

      - name: Save to repository
        env:
          GH_TOKEN: ${{ secrets.GH_TOKEN }}
        run: |
          echo GH_TOKEN: "${GH_TOKEN}"
          git config --global user.name 'github-actions'
          git config --local user.email "action@github.com"
          git add .
          git commit -m "Add results"
          git push
