document.addEventListener('DOMContentLoaded', () => {
    const loanForm = document.getElementById('loanForm');
    const submitBtn = document.getElementById('submitBtn');
    const resetFormBtn = document.getElementById('resetFormBtn');
    const steppedLoader = document.getElementById('steppedLoader');
    const steppedMessage = document.getElementById('steppedMessage');
    const resultCard = document.getElementById('resultCard');
    
    const loanAmountInput = document.getElementById('loanAmount');
    const loanAmountSlider = document.getElementById('loanAmountSlider');

    const themeToggleBtn = document.getElementById('themeToggleBtn');
    const themeIcon = document.getElementById('themeIcon');
    
    const analyticsBtn = document.getElementById('analyticsBtn');
    const navAnalyticsBtn = document.getElementById('navAnalyticsBtn');
    const navDocsBtn = document.getElementById('navDocsBtn');
    const navHistoryBtn = document.getElementById('navHistoryBtn');
    const historyBtn = document.getElementById('historyBtn');

    const historySearchInput = document.getElementById('historySearchInput');
    const historyStatusFilter = document.getElementById('historyStatusFilter');
    const historySortSelect = document.getElementById('historySortSelect');

    let gaugeChart = null;

    // Initialize Bootstrap Tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));

    // Theme Switcher
    const currentTheme = localStorage.getItem('smart_lender_theme') || 'dark';
    document.documentElement.setAttribute('data-theme', currentTheme);
    updateThemeIcon(currentTheme);

    themeToggleBtn.addEventListener('click', () => {
        const theme = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('smart_lender_theme', theme);
        updateThemeIcon(theme);
    });

    // Initial default call
    setTimeout(() => {
        updateLakhsDisplay();
        updateRealTimePrecalc();
    }, 100);

    function updateThemeIcon(theme) {
        themeIcon.className = theme === 'light' ? 'fas fa-moon' : 'fas fa-sun';
    }

    // Reset Form Handler
    if (resetFormBtn) {
        resetFormBtn.addEventListener('click', () => {
            loanForm.reset();
            loanForm.classList.remove('was-validated');
            loanAmountSlider.value = 150;
            loanAmountInput.value = 150;
            resultCard.classList.add('d-none');
            updateLakhsDisplay();
            updateRealTimePrecalc();
        });
    }

    const loanAmountLakhsDisplay = document.getElementById('loanAmountLakhsDisplay');

    function updateLakhsDisplay() {
        const val = parseFloat(loanAmountInput.value) || 0;
        const totalRupees = val * 1000;
        if (totalRupees >= 100000) {
            const lakhs = totalRupees / 100000;
            loanAmountLakhsDisplay.textContent = `₹${lakhs.toFixed(2)} Lakhs (₹${totalRupees.toLocaleString('en-IN')})`;
        } else {
            loanAmountLakhsDisplay.textContent = `₹${totalRupees.toLocaleString('en-IN')}`;
        }
    }

    // Loan Amount Input <-> Slider Sync
    loanAmountInput.addEventListener('input', () => {
        loanAmountSlider.value = loanAmountInput.value;
        updateLakhsDisplay();
        updateRealTimePrecalc();
    });

    loanAmountSlider.addEventListener('input', () => {
        loanAmountInput.value = loanAmountSlider.value;
        updateLakhsDisplay();
        updateRealTimePrecalc();
    });

    const applicantIncomeInput = document.getElementById('applicantIncome');
    const coapplicantIncomeInput = document.getElementById('coapplicantIncome');
    const loanTermSelect = document.getElementById('loanTerm');
    const creditHistorySelect = document.getElementById('creditHistory');

    const preCalcWidget = document.getElementById('preCalcWidget');
    const preCalcLTI = document.getElementById('preCalcLTI');
    const preCalcMonthly = document.getElementById('preCalcMonthly');
    const preCalcDTI = document.getElementById('preCalcDTI');
    const creditHistoryVetoWarning = document.getElementById('creditHistoryVetoWarning');
    const dtiVetoWarning = document.getElementById('dtiVetoWarning');

    function updateRealTimePrecalc() {
        const appIncome = parseFloat(applicantIncomeInput.value) || 0;
        const coIncome = parseFloat(coapplicantIncomeInput.value) || 0;
        const loanAmt = parseFloat(loanAmountInput.value) || 0;
        const term = parseFloat(loanTermSelect.value) || 360;
        const creditHist = creditHistorySelect.value;

        if (appIncome <= 0 && loanAmt <= 0) {
            preCalcWidget.classList.add('d-none');
            return;
        }

        preCalcWidget.classList.remove('d-none');

        const totalIncome = appIncome + coIncome;
        const annualIncome = totalIncome * 12;
        const loanAmtActual = loanAmt * 1000;
        const lti = totalIncome > 0 ? (loanAmtActual / (annualIncome + 1e-5)) : 0;
        const estMonthly = term > 0 ? (loanAmtActual / term) : 0;
        const dti = totalIncome > 0 ? ((estMonthly / (totalIncome + 1e-5)) * 100) : 0;

        preCalcLTI.textContent = lti.toFixed(2) + 'x';
        preCalcMonthly.textContent = '₹' + estMonthly.toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
        preCalcDTI.textContent = dti.toFixed(1) + '%';

        // Check Credit Veto Alert
        if (creditHist === '0.0') {
            creditHistoryVetoWarning.classList.remove('d-none');
        } else {
            creditHistoryVetoWarning.classList.add('d-none');
        }

        // Check DTI Veto Alert
        if (dti > 85.0) {
            dtiVetoWarning.classList.remove('d-none');
        } else {
            dtiVetoWarning.classList.add('d-none');
        }
    }

    [applicantIncomeInput, coapplicantIncomeInput, loanTermSelect, creditHistorySelect].forEach(el => {
        if (el) el.addEventListener('input', updateRealTimePrecalc);
    });

    // Analytics Modal Data Fetcher
    const openAnalyticsModal = async () => {
        const modal = new bootstrap.Modal(document.getElementById('analyticsModal'));
        modal.show();
        
        try {
            const res = await fetch('/model-telemetry');
            const data = await res.json();
            if (data.success) {
                document.getElementById('telemetryModelName').textContent = data.model_name;
                document.getElementById('telemetryAccuracy').textContent = `${(data.metrics.accuracy * 100).toFixed(1)}%`;
                document.getElementById('telemetryF1').textContent = `${(data.metrics.f1_score * 100).toFixed(1)}%`;
                document.getElementById('telemetryAUC').textContent = `${(data.metrics.roc_auc * 100).toFixed(1)}%`;

                // Render Model Comparison Bar Chart
                const chartCanvas = document.getElementById('modelTelemetryBarChart');
                if (chartCanvas && data.all_models_benchmarks) {
                    const ctxBar = chartCanvas.getContext('2d');
                    if (window.telemetryBarChartObj) window.telemetryBarChartObj.destroy();
                    
                    const labels = Object.keys(data.all_models_benchmarks);
                    const accuracies = labels.map(l => (data.all_models_benchmarks[l].accuracy * 100).toFixed(1));
                    const f1Scores = labels.map(l => (data.all_models_benchmarks[l].f1_score * 100).toFixed(1));

                    window.telemetryBarChartObj = new Chart(ctxBar, {
                        type: 'bar',
                        data: {
                            labels: labels,
                            datasets: [
                                {
                                    label: 'Accuracy (%)',
                                    data: accuracies,
                                    backgroundColor: 'rgba(23, 162, 184, 0.75)',
                                    borderColor: 'rgba(23, 162, 184, 1)',
                                    borderWidth: 1
                                },
                                {
                                    label: 'F1 Score (%)',
                                    data: f1Scores,
                                    backgroundColor: 'rgba(255, 193, 7, 0.75)',
                                    borderColor: 'rgba(255, 193, 7, 1)',
                                    borderWidth: 1
                                }
                            ]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            plugins: {
                                legend: {
                                    labels: { color: '#ffffff' }
                                }
                            },
                            scales: {
                                x: {
                                    grid: { color: 'rgba(255,255,255,0.05)' },
                                    ticks: { color: '#ffffff', font: { size: 10 } }
                                },
                                y: {
                                    grid: { color: 'rgba(255,255,255,0.05)' },
                                    ticks: { color: '#ffffff' },
                                    min: 0,
                                    max: 100
                                }
                            }
                        }
                    });
                }

                // Render Model Comparison Table
                const tbody = document.getElementById('modelComparisonTbody');
                if (tbody && data.all_models_benchmarks) {
                    let tableHtml = '';
                    for (const [mName, mMetrics] of Object.entries(data.all_models_benchmarks)) {
                        const isBest = mName === data.model_name;
                        tableHtml += `
                            <tr class="${isBest ? 'table-success text-dark fw-bold' : ''}">
                                <td>${mName} ${isBest ? '<span class="badge bg-success ms-1">Best</span>' : ''}</td>
                                <td>${(mMetrics.accuracy * 100).toFixed(1)}%</td>
                                <td>${(mMetrics.precision * 100).toFixed(1)}%</td>
                                <td>${(mMetrics.recall * 100).toFixed(1)}%</td>
                                <td>${(mMetrics.f1_score * 100).toFixed(1)}%</td>
                                <td>${(mMetrics.roc_auc * 100).toFixed(1)}%</td>
                                <td>${mMetrics.train_time_sec} s</td>
                            </tr>
                        `;
                    }
                    tbody.innerHTML = tableHtml;
                }
            }
        } catch (e) {
            console.error("Telemetry fetch failed", e);
        }
    };

    if (analyticsBtn) analyticsBtn.addEventListener('click', openAnalyticsModal);
    if (navAnalyticsBtn) navAnalyticsBtn.addEventListener('click', (e) => { e.preventDefault(); openAnalyticsModal(); });

    // Documentation Modal Launcher
    if (navDocsBtn) {
        navDocsBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const modal = new bootstrap.Modal(document.getElementById('docsModal'));
            modal.show();
        });
    }

    // History Modal Management
    const openHistoryModal = () => {
        renderHistory();
        const modal = new bootstrap.Modal(document.getElementById('historyModal'));
        modal.show();
    };

    if (historyBtn) historyBtn.addEventListener('click', openHistoryModal);
    if (navHistoryBtn) navHistoryBtn.addEventListener('click', (e) => { e.preventDefault(); openHistoryModal(); });

    document.getElementById('clearHistoryBtn').addEventListener('click', () => {
        localStorage.removeItem('smart_lender_history');
        renderHistory();
    });

    if (historySearchInput) historySearchInput.addEventListener('input', renderHistory);
    if (historyStatusFilter) historyStatusFilter.addEventListener('change', renderHistory);
    if (historySortSelect) historySortSelect.addEventListener('change', renderHistory);

    function getHistory() {
        return JSON.parse(localStorage.getItem('smart_lender_history') || '[]');
    }

    function saveToHistory(record) {
        let history = getHistory();
        history.unshift(record);
        if (history.length > 20) history = history.slice(0, 20);
        localStorage.setItem('smart_lender_history', JSON.stringify(history));
    }

    function renderHistory() {
        const container = document.getElementById('historyContainer');
        let history = getHistory();
        if (history.length === 0) {
            container.innerHTML = `<p class="text-secondary text-center">No past application evaluations recorded in local memory.</p>`;
            return;
        }

        const query = historySearchInput ? historySearchInput.value.toLowerCase() : '';
        const statusFilter = historyStatusFilter ? historyStatusFilter.value : 'ALL';
        const sortSelect = historySortSelect ? historySortSelect.value : 'NEWEST';

        if (query) {
            history = history.filter(h => 
                h.inputs.ApplicantIncome.toString().includes(query) || 
                h.inputs.LoanAmount.toString().includes(query)
            );
        }

        if (statusFilter !== 'ALL') {
            history = history.filter(h => h.status === statusFilter);
        }

        if (sortSelect === 'HIGHEST_PROB') {
            history.sort((a, b) => b.probability - a.probability);
        }

        if (history.length === 0) {
            container.innerHTML = `<p class="text-secondary text-center">No matching evaluation records found.</p>`;
            return;
        }

        let html = '<div class="list-group list-group-flush rounded-3">';
        history.forEach((item, idx) => {
            const isApp = item.status === 'APPROVED';
            html += `
                <div class="list-group-item bg-dark bg-opacity-40 border-secondary border-opacity-25 text-white mb-2 rounded-3 p-3">
                    <div class="d-flex justify-content-between align-items-center mb-2">
                        <span class="badge ${isApp ? 'bg-success' : 'bg-danger'} px-3 py-2 fs-6">${item.status} (${item.probability}%)</span>
                        <small class="text-muted">${item.timestamp}</small>
                    </div>
                    <p class="mb-2 small text-light">Income: ₹${item.inputs.ApplicantIncome} | Loan: ₹${item.inputs.LoanAmount}k | Credit: ${item.inputs.Credit_History}</p>
                    <button class="btn btn-sm btn-outline-info reuse-btn" data-idx="${idx}"><i class="fas fa-redo me-1"></i> Reuse Form Inputs</button>
                </div>
            `;
        });
        html += '</div>';
        container.innerHTML = html;

        document.querySelectorAll('.reuse-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const idx = e.currentTarget.getAttribute('data-idx');
                const selected = history[idx];
                if (selected && selected.inputs) {
                    populateForm(selected.inputs);
                    bootstrap.Modal.getInstance(document.getElementById('historyModal')).hide();
                }
            });
        });
    }

    function populateForm(inputs) {
        for (const key in inputs) {
            const el = document.getElementById(key.charAt(0).toLowerCase() + key.slice(1)) || 
                       document.getElementById(key) ||
                       (key === 'Loan_Amount_Term' ? document.getElementById('loanTerm') : null) ||
                       (key === 'Self_Employed' ? document.getElementById('selfEmployed') : null) ||
                       (key === 'Credit_History' ? document.getElementById('creditHistory') : null) ||
                       (key === 'Property_Area' ? document.getElementById('propertyArea') : null);
            if (el) {
                el.value = inputs[key];
            }
        }
        loanAmountSlider.value = loanAmountInput.value;
        updateLakhsDisplay();
        updateRealTimePrecalc();
    }

    // Form Submission with Stepped Loader & Hyper-Polish Effects
    loanForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        if (!loanForm.checkValidity()) {
            loanForm.classList.add('was-validated');
            return;
        }

        const formData = {
            Gender: document.getElementById('gender').value,
            Married: document.getElementById('married').value,
            Dependents: document.getElementById('dependents').value,
            Education: document.getElementById('education').value,
            Self_Employed: document.getElementById('selfEmployed').value,
            ApplicantIncome: parseFloat(document.getElementById('applicantIncome').value),
            CoapplicantIncome: parseFloat(document.getElementById('coapplicantIncome').value || 0),
            LoanAmount: parseFloat(document.getElementById('loanAmount').value),
            Loan_Amount_Term: parseFloat(document.getElementById('loanTerm').value),
            Credit_History: parseFloat(document.getElementById('creditHistory').value),
            Property_Area: document.getElementById('propertyArea').value
        };

        submitBtn.disabled = true;
        steppedLoader.classList.remove('d-none');
        resultCard.classList.add('d-none');

        const steps = [
            "Checking Credit History...",
            "Evaluating Income...",
            "Verifying Employment...",
            "Calculating Risk Score...",
            "Running ML Model...",
            "Generating Recommendation..."
        ];
        
        for (let i = 0; i < steps.length; i++) {
            steppedMessage.textContent = steps[i];
            await new Promise(r => setTimeout(r, 180));
        }

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            });

            const result = await response.json();

            submitBtn.disabled = false;
            steppedLoader.classList.add('d-none');

            if (result.success) {
                displayResult(result, formData);
                saveToHistory({
                    status: result.status,
                    probability: result.probability,
                    timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
                    inputs: formData
                });

                if (result.eligible && typeof confetti === 'function') {
                    confetti({
                        particleCount: 100,
                        spread: 70,
                        origin: { y: 0.6 }
                    });
                }
            } else {
                displayError(result.error || 'An error occurred during risk evaluation.');
            }
        } catch (error) {
            submitBtn.disabled = false;
            steppedLoader.classList.add('d-none');
            displayError('Network communication timeout. Please verify Flask server status.');
        }
    });

    function displayResult(res, rawInputs) {
        resultCard.classList.remove('d-none');
        const isApp = res.eligible;
        
        let explanationsHtml = '';
        if (res.explanations && res.explanations.length > 0) {
            explanationsHtml = `<h6 class="fw-bold mt-3 mb-2 text-start text-light">${isApp ? 'Why Approved?' : 'Suggestions to Improve Eligibility'}</h6><ul class="list-unstyled text-start small mb-3">`;
            res.explanations.forEach(exp => {
                explanationsHtml += `<li class="mb-1 ${isApp ? 'text-success fw-semibold' : 'text-warning fw-semibold'}">${exp}</li>`;
            });
            explanationsHtml += `</ul>`;
        }

        let insightsHtml = '';
        if (res.smart_insights && res.smart_insights.length > 0) {
            insightsHtml = `<h6 class="fw-bold mt-3 mb-2 text-start text-light"><i class="fas fa-lightbulb text-warning me-1"></i> Smart Financial Insights & Recommendations</h6><ul class="list-unstyled text-start small mb-0 text-light">`;
            res.smart_insights.forEach(ins => {
                insightsHtml += `<li class="mb-1 text-light"><i class="fas fa-chevron-right me-1 text-info"></i> ${ins}</li>`;
            });
            insightsHtml += `</ul>`;
        }

        resultCard.innerHTML = `
            <div class="p-3 p-md-4 ${isApp ? 'result-approved-banner' : 'result-rejected-banner'} text-center position-relative">
                <div class="row align-items-center">
                    <div class="col-md-5 mb-3 mb-md-0">
                        <div class="gauge-canvas-container">
                            <canvas id="probabilityGaugeCanvas"></canvas>
                        </div>
                    </div>
                    <div class="col-md-7 text-md-start">
                        <div class="d-flex flex-wrap gap-1 align-items-center justify-content-center justify-content-md-start mb-2">
                            <span class="badge ${isApp ? 'bg-success' : 'bg-danger'} px-3 py-2 fs-6">${res.status}</span>
                            <span class="badge bg-info bg-opacity-20 text-info px-3 py-2 fs-6">${res.confidence_level}</span>
                            <span class="badge bg-secondary px-3 py-2 fs-6">${res.risk_level || 'Evaluated Risk'}</span>
                        </div>
                        <h3 class="fw-bold mb-1 text-white fs-4 fs-md-3">${res.status === 'APPROVED' ? 'Application Approved!' : 'Application Declined'}</h3>
                        <p class="fs-6 text-light opacity-75 mb-3">${res.message}</p>
                        <div class="d-flex flex-wrap gap-2 small fw-semibold align-items-center justify-content-center justify-content-md-start">
                            <span class="badge bg-dark bg-opacity-60 text-info border border-info border-opacity-25 px-3 py-2 fs-6"><i class="fas fa-microchip me-1 text-info"></i> ${res.model_used}</span>
                            <span class="badge bg-dark bg-opacity-60 text-warning border border-warning border-opacity-25 px-3 py-2 fs-6"><i class="fas fa-bolt me-1 text-warning"></i> ${res.prediction_time_ms} ms</span>
                        </div>
                    </div>
                </div>

                ${explanationsHtml}
                ${insightsHtml}

                <div class="mt-4 pt-3 border-top border-secondary border-opacity-25 d-flex flex-wrap justify-content-center gap-2">
                    <button class="btn btn-sm btn-outline-light rounded-pill px-3" id="printResultBtn"><i class="fas fa-print me-1"></i> Print Result</button>
                    <button class="btn btn-sm btn-outline-info rounded-pill px-3" id="downloadJsonBtn"><i class="fas fa-file-code me-1"></i> Export JSON</button>
                    <button class="btn btn-sm btn-outline-success rounded-pill px-3" id="downloadCsvBtn"><i class="fas fa-file-csv me-1"></i> Export CSV</button>
                </div>
            </div>
        `;

        const ctx = document.getElementById('probabilityGaugeCanvas').getContext('2d');
        if (gaugeChart) gaugeChart.destroy();

        gaugeChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Probability Index', 'Risk Margin'],
                datasets: [{
                    data: [res.probability, 100 - res.probability],
                    backgroundColor: [isApp ? '#10b981' : '#f43f5e', 'rgba(255,255,255,0.08)'],
                    borderWidth: 0
                }]
            },
            options: {
                rotation: -90,
                circumference: 180,
                cutout: '75%',
                plugins: {
                    legend: { display: false },
                    tooltip: { enabled: false }
                }
            },
            plugins: [{
                id: 'gaugeText',
                beforeDraw: (chart) => {
                    const width = chart.width, height = chart.height, ctx = chart.ctx;
                    ctx.restore();
                    ctx.font = "bold 1.8rem Outfit, sans-serif";
                    ctx.textBaseline = "middle";
                    ctx.fillStyle = isApp ? '#10b981' : '#f43f5e';
                    const text = res.probability + "%", textX = Math.round((width - ctx.measureText(text).width) / 2), textY = height / 1.4;
                    ctx.fillText(text, textX, textY);
                    ctx.save();
                }
            }]
        });

        resultCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

        document.getElementById('printResultBtn').addEventListener('click', () => window.print());
        document.getElementById('downloadJsonBtn').addEventListener('click', () => {
            const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(res, null, 2));
            const downloadAnchor = document.createElement('a');
            downloadAnchor.setAttribute("href", dataStr);
            downloadAnchor.setAttribute("download", `smartlender_assessment_${Date.now()}.json`);
            document.body.appendChild(downloadAnchor);
            downloadAnchor.click();
            downloadAnchor.remove();
        });
        document.getElementById('downloadCsvBtn').addEventListener('click', () => {
            const csvRows = [
                ['Field', 'Value'],
                ['Status', res.status],
                ['Probability', res.probability + '%'],
                ['Confidence', res.confidence_level],
                ['Risk Level', res.risk_level],
                ['Model Used', res.model_used],
                ['Prediction Time (ms)', res.prediction_time_ms]
            ];
            const csvContent = "data:text/csv;charset=utf-8," + csvRows.map(e => e.join(",")).join("\n");
            const encodedUri = encodeURI(csvContent);
            const link = document.createElement("a");
            link.setAttribute("href", encodedUri);
            link.setAttribute("download", `smartlender_assessment_${Date.now()}.csv`);
            document.body.appendChild(link);
            link.click();
            link.remove();
        });
    }

    function displayError(errMsg) {
        resultCard.classList.remove('d-none');
        resultCard.innerHTML = `
            <div class="alert alert-danger d-flex align-items-center rounded-4 shadow-sm" role="alert">
                <i class="fas fa-triangle-exclamation fa-2x me-3"></i>
                <div>
                    <h5 class="alert-heading mb-1 fw-bold">Evaluation Exception</h5>
                    <p class="mb-0">${errMsg}</p>
                </div>
            </div>
        `;
    }
});
