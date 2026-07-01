# Repository Folder Structure Explanation

The directory structure below details the purpose of each modular folder in the **SmartLender AI** project:

```
c:\project\
│
├── dataset/                     # Contains raw/synthetic tabular datasets (.csv)
│   └── loan_data.csv            # 614-record training dataset
│
├── model/                       # Serialized machine learning output artifacts
│   └── loan_model.pkl           # Packed joblib classifier, encoders & scaler
│
├── static/                      # Static assets served by the web engine
│   ├── css/                     # Vanilla CSS dark navy stylesheet
│   │   └── style.css            # Dark mode, glassmorphism, animations, responsive rules
│   ├── js/                      # Frontend JavaScript controller files
│   │   └── main.js              # Fetch queries, stepped loader, history, gauge, exports
│   └── screenshots/             # Visual analytics charts generated during training
│       ├── confusion_matrix.png # True vs Predicted heatmap
│       ├── roc_curve.png        # Receiver Operating Characteristic curve
│       └── feature_importance.png # Key classification decision drivers
│
├── templates/                   # Flask HTML view templates
│   └── index.html               # Main SPA entry point
│
├── testing/                     # Automated and manual QA assets
│   ├── unit_test_examples.py    # Unittest file executing route assertions
│   └── manual_test_cases.md     # Step-by-step test matrix
│
├── docs/                        # Complete 8-Phase SDLC documentation
│   └── [1_to_8_folders]/        # Segregated PDF-ready markdown archives
│
├── config.py                    # Configurations (Ports, debug settings, file paths)
├── app.py                       # Main Flask web application
├── train_model.py               # Model training script
└── requirements.txt             # Project library dependencies
```
- **Segregation Rationale:** Keeping static assets and templates separate ensures clean Flask routing. Having a dedicated `testing/` directory prevents QA code from mixing with production application files.
