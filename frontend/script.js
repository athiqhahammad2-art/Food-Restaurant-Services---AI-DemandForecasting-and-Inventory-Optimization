// API Configuration
const API_BASE_URL = 'http://localhost:5000/api';

// Initialize Charts
let charts = {};

// Navigation handling
document.querySelectorAll('.nav-item').forEach(item => {
    item.addEventListener('click', (e) => {
        e.preventDefault();
        
        // Remove active class from all nav items
        document.querySelectorAll('.nav-item').forEach(nav => nav.classList.remove('active'));
        item.classList.add('active');
        
        // Hide all content sections
        document.querySelectorAll('.content-section').forEach(section => {
            section.classList.remove('active');
        });
        
        // Show selected section
        const section = item.getAttribute('data-section');
        const selectedSection = document.getElementById(section);
        if (selectedSection) {
            selectedSection.classList.add('active');
            updatePageHeader(section);
            initializeCharts(section);
        }
    });
});

// Update page header
function updatePageHeader(section) {
    const titles = {
        overview: { title: 'Dashboard', subtitle: 'Real-time inventory and demand insights' },
        demand: { title: 'Demand Forecasting', subtitle: 'AI-powered demand predictions' },
        inventory: { title: 'Inventory Optimization', subtitle: 'Smart stock management' },
        analytics: { title: 'Analytics & Trends', subtitle: 'Historical analysis and insights' },
        suppliers: { title: 'Suppliers', subtitle: 'Manage your suppliers' },
        menu: { title: 'Menu Items', subtitle: 'Manage menu items' }
    };
    
    document.getElementById('page-title').textContent = titles[section].title;
    document.getElementById('page-subtitle').textContent = titles[section].subtitle;
}

// Initialize Charts
function initializeCharts(section) {
    if (section === 'overview' && !charts.salesVsForecast) {
        initOverviewCharts();
    } else if (section === 'demand' && !charts.demandForecast) {
        initDemandCharts();
    } else if (section === 'inventory' && !charts.eoq) {
        initInventoryCharts();
    } else if (section === 'analytics' && !charts.salesTrends) {
        initAnalyticsCharts();
    }
}

// Overview Charts
function initOverviewCharts() {
    // Sales vs Forecast Chart
    const ctx1 = document.getElementById('salesVsForecastChart');
    if (ctx1) {
        charts.salesVsForecast = new Chart(ctx1, {
            type: 'line',
            data: {
                labels: ['Jun 25', 'Jun 26', 'Jun 27', 'Jun 28', 'Jun 29', 'Jun 30', 'Jul 1'],
                datasets: [
                    {
                        label: 'Actual Sales',
                        data: [120, 135, 145, 128, 155, 168, 172],
                        borderColor: '#667eea',
                        backgroundColor: 'rgba(102, 126, 234, 0.1)',
                        borderWidth: 3,
                        fill: true,
                        tension: 0.4,
                        pointRadius: 5,
                        pointBackgroundColor: '#667eea'
                    },
                    {
                        label: 'Forecasted Demand',
                        data: [118, 132, 148, 130, 152, 165, 170],
                        borderColor: '#764ba2',
                        backgroundColor: 'rgba(118, 75, 162, 0.1)',
                        borderWidth: 3,
                        fill: true,
                        tension: 0.4,
                        pointRadius: 5,
                        pointBackgroundColor: '#764ba2'
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: {
                        position: 'top',
                        labels: { font: { size: 13 }, padding: 20 }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: { drawBorder: false }
                    },
                    x: {
                        grid: { display: false }
                    }
                }
            }
        });
    }

    // Inventory Chart
    const ctx2 = document.getElementById('inventoryChart');
    if (ctx2) {
        charts.inventory = new Chart(ctx2, {
            type: 'doughnut',
            data: {
                labels: ['Optimal Stock', 'Low Stock', 'Critical'],
                datasets: [{
                    data: [65, 25, 10],
                    backgroundColor: ['#43e97b', '#ffa502', '#ff6b6b'],
                    borderColor: '#ffffff',
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: {
                        position: 'right',
                        labels: { font: { size: 13 }, padding: 20 }
                    }
                }
            }
        });
    }
}

// Demand Forecasting Charts
function initDemandCharts() {
    const ctx1 = document.getElementById('demandForecastChart');
    if (ctx1) {
        charts.demandForecast = new Chart(ctx1, {
            type: 'line',
            data: {
                labels: ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7', 'Day 8', 'Day 9', 'Day 10'],
                datasets: [
                    {
                        label: 'Forecasted Demand',
                        data: [145, 168, 152, 175, 182, 195, 188, 205, 198, 210],
                        borderColor: '#667eea',
                        backgroundColor: 'rgba(102, 126, 234, 0.1)',
                        borderWidth: 3,
                        fill: true,
                        tension: 0.4,
                        pointRadius: 5
                    },
                    {
                        label: 'Upper Confidence Band',
                        data: [162, 185, 169, 192, 199, 212, 205, 222, 215, 227],
                        borderColor: '#764ba2',
                        borderWidth: 1,
                        borderDash: [5, 5],
                        fill: false,
                        tension: 0.4
                    },
                    {
                        label: 'Lower Confidence Band',
                        data: [128, 151, 135, 158, 165, 178, 171, 188, 181, 193],
                        borderColor: '#764ba2',
                        borderWidth: 1,
                        borderDash: [5, 5],
                        fill: false,
                        tension: 0.4
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    filler: { propagate: true },
                    legend: {
                        position: 'top',
                        labels: { font: { size: 13 }, padding: 20 }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: { drawBorder: false }
                    }
                }
            }
        });
    }
}

// Inventory Optimization Charts
function initInventoryCharts() {
    const ctx1 = document.getElementById('eoqChart');
    if (ctx1) {
        charts.eoq = new Chart(ctx1, {
            type: 'bar',
            data: {
                labels: ['Chicken Breast', 'Tomatoes', 'Flour', 'Rice', 'Cheese'],
                datasets: [{
                    label: 'Economic Order Quantity (kg)',
                    data: [28, 35, 40, 50, 25],
                    backgroundColor: [
                        'rgba(102, 126, 234, 0.8)',
                        'rgba(118, 75, 162, 0.8)',
                        'rgba(245, 87, 108, 0.8)',
                        'rgba(67, 233, 123, 0.8)',
                        'rgba(255, 165, 2, 0.8)'
                    ],
                    borderRadius: 8
                }]
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: { display: true }
                },
                scales: {
                    x: {
                        beginAtZero: true,
                        grid: { drawBorder: false }
                    }
                }
            }
        });
    }

    const ctx2 = document.getElementById('safetyStockChart');
    if (ctx2) {
        charts.safetyStock = new Chart(ctx2, {
            type: 'radar',
            data: {
                labels: ['Chicken', 'Tomatoes', 'Flour', 'Rice', 'Cheese', 'Butter'],
                datasets: [{
                    label: 'Safety Stock Levels',
                    data: [8, 6, 4, 5, 3, 2],
                    borderColor: '#667eea',
                    backgroundColor: 'rgba(102, 126, 234, 0.2)',
                    borderWidth: 2,
                    pointRadius: 5,
                    pointBackgroundColor: '#667eea'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: {
                        position: 'top',
                        labels: { font: { size: 13 } }
                    }
                },
                scales: {
                    r: {
                        beginAtZero: true
                    }
                }
            }
        });
    }
}

// Analytics Charts
function initAnalyticsCharts() {
    const ctx1 = document.getElementById('salesTrendsChart');
    if (ctx1) {
        charts.salesTrends = new Chart(ctx1, {
            type: 'area',
            data: {
                labels: Array.from({length: 30}, (_, i) => `Day ${i + 1}`),
                datasets: [{
                    label: 'Daily Sales',
                    data: Array.from({length: 30}, () => Math.floor(Math.random() * 200 + 100)),
                    borderColor: '#667eea',
                    backgroundColor: 'rgba(102, 126, 234, 0.2)',
                    borderWidth: 2,
                    fill: true,
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: { display: true }
                }
            }
        });
    }

    const ctx2 = document.getElementById('topItemsChart');
    if (ctx2) {
        charts.topItems = new Chart(ctx2, {
            type: 'horizontalBar',
            indexAxis: 'y',
            data: {
                labels: ['Burger Deluxe', 'Caesar Salad', 'Margherita Pizza', 'Pasta Carbonara', 'Fried Chicken'],
                datasets: [{
                    label: 'Sales (Units)',
                    data: [234, 189, 312, 156, 198],
                    backgroundColor: [
                        '#667eea',
                        '#764ba2',
                        '#f5576c',
                        '#43e97b',
                        '#ffa502'
                    ]
                }]
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: { display: true }
                }
            }
        });
    }

    const ctx3 = document.getElementById('turnoverChart');
    if (ctx3) {
        charts.turnover = new Chart(ctx3, {
            type: 'line',
            data: {
                labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
                datasets: [{
                    label: 'Inventory Turnover Ratio',
                    data: [4.2, 4.5, 4.8, 5.1],
                    borderColor: '#43e97b',
                    backgroundColor: 'rgba(67, 233, 123, 0.1)',
                    borderWidth: 3,
                    fill: true,
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: { display: true }
                }
            }
        });
    }

    const ctx4 = document.getElementById('wasteChart');
    if (ctx4) {
        charts.waste = new Chart(ctx4, {
            type: 'doughnut',
            data: {
                labels: ['Used', 'Waste', 'Spoilage'],
                datasets: [{
                    data: [92, 5, 3],
                    backgroundColor: ['#43e97b', '#ffa502', '#ff6b6b'],
                    borderColor: '#ffffff',
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: {
                        position: 'right',
                        labels: { font: { size: 13 } }
                    }
                }
            }
        });
    }
}

// Fetch and display data from API
async function fetchDashboardData() {
    try {
        const response = await axios.get(`${API_BASE_URL}/analytics/dashboard`);
        updateDashboardMetrics(response.data);
    } catch (error) {
        console.error('Error fetching dashboard data:', error);
    }
}

// Update dashboard metrics
function updateDashboardMetrics(data) {
    document.getElementById('total-sales').textContent = `$${data.total_sales?.toLocaleString() || '24,500'}`;
    document.getElementById('items-stock').textContent = data.items_in_stock || '1,245';
    document.getElementById('low-stock').textContent = data.low_stock_items || '23';
    document.getElementById('forecast-accuracy').textContent = `${data.forecast_accuracy || '94.2'}%`;
}

// Refresh data
function refreshData() {
    console.log('Refreshing data...');
    fetchDashboardData();
    initializeCharts(getCurrentSection());
}

// Get current section
function getCurrentSection() {
    const activeSection = document.querySelector('.content-section.active');
    return activeSection ? activeSection.id : 'overview';
}

// Generate Purchase Orders
function generateOrders() {
    alert('Generating purchase orders...');
    console.log('Generate purchase orders clicked');
}

// Order Item
function orderItem(item) {
    alert(`Order placed for ${item}`);
    console.log(`Order item: ${item}`);
}

// Add Supplier
function addSupplier() {
    const supplierName = prompt('Enter supplier name:');
    if (supplierName) {
        console.log(`Adding supplier: ${supplierName}`);
        alert(`Supplier "${supplierName}" added successfully!`);
    }
}

// Add Menu Item
function addMenuItem() {
    const itemName = prompt('Enter menu item name:');
    if (itemName) {
        console.log(`Adding menu item: ${itemName}`);
        alert(`Menu item "${itemName}" added successfully!`);
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    initOverviewCharts();
    fetchDashboardData();
    
    // Set today's date as default
    const today = new Date().toISOString().split('T')[0];
    document.getElementById('date-filter').value = today;
});

// Handle window resize for responsive charts
window.addEventListener('resize', () => {
    Object.values(charts).forEach(chart => {
        if (chart) chart.resize();
    });
});
