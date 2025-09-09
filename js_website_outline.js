// Load Cbbontop rankings when page opens
fetch('cbbontop_rankings.json')
    .then(response => response.json())
    .then(data => {
        const tableHTML = `
            <table class="rankings-table">
                <thead>
                    <tr>
                        <th>Rank</th>
                        <th>School</th>
                        <th>Conference</th>
                        <th>Record</th>
                        <th>Cbbontop Score</th>
                    </tr>
                </thead>
                <tbody>
                    ${data.map(team => `
                        <tr>
                            <td>${team.Cbbontop_Rank}</td>
                            <td>${team.School}</td>
                            <td>${team.Conference}</td>
                            <td>${team.Record}</td>
                            <td>${team.Cbbontop_Score}</td>
                        </tr>
                    `).join('')}
                </tbody>
            </table>
        `;
        document.getElementById('rankings-display').innerHTML = tableHTML;
    })
    .catch(error => {
        document.getElementById('rankings-display').innerHTML = 
            '<p style="color: #d32f2f; text-align: center;">Please run the Python script first to generate rankings.</p>';
    });
/*
let btnClick = document.querySelector("GamePredictionsButton")
btnClick.addEventListener("click", () => {
    window.location.href = "game_predictions.html";
    
});
*/

/// Make buttons work

let btnClick1 = document.querySelector("GamePredictionsButton")
btnClick1.addEventListener("click", () => {
    window.location.href = "game_predictions.html";
})

let btnClick2 = document.querySelector("DeathBlowButton")
btnClick2.addEventListener("click", () => {
    window.location.href = "death_blow.html";
})

let btnClick3 = document.querySelector("VisualizationButton")
btnClick3.addEventListener("click", () => {
    window.location.href = "data_visualizations.html";
})

let btnClick4 = document.querySelector("StatsButton")
btnClick4.addEventListener("click", () => {
    window.location.href = "stat_leaders.html";
})

let btnClick5 = document.querySelector("StreaksButton")
btnClick5.addEventListener("click", () => {
    window.location.href = "stat_streaks.html";
})

let btnClick6 = document.querySelector("BracketButton")
btnClick6.addEventListener("click", () => {
    window.location.href = "bracket_builder.html";
})

let btnClick7 = document.querySelector("MainButton")
btnClick7.addEventListener("click", () => {
    window.location.href = "main_page.html";
})

// Mobile hamburger menu functionality
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const navigationMenu = document.getElementById('navigation-menu');
    
    if (mobileMenuBtn && navigationMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            navigationMenu.classList.toggle('active');
            
            // Change button text
            if (navigationMenu.classList.contains('active')) {
                mobileMenuBtn.textContent = '✕ Close';
            } else {
                mobileMenuBtn.textContent = '☰ Menu';
            }
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!mobileMenuBtn.contains(event.target) && !navigationMenu.contains(event.target)) {
                navigationMenu.classList.remove('active');
                mobileMenuBtn.textContent = '☰ Menu';
            }
        });
    }
});