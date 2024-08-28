document.addEventListener("DOMContentLoaded", function() {
    // Hide/Show Columns
    const checkboxes = document.querySelectorAll('.form-check-input');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const target = this.getAttribute('data-target');
            const elements = document.querySelectorAll(`[data-column="${target}"]`);
            elements.forEach(element => {
                element.style.display = this.checked ? '' : 'none';
            });
        });
    });

    // Add Filter Input
    const addButton = document.getElementById('addButton');
    const inputContainer = document.getElementById('inputContainer');
    const submitButton = document.getElementById('submitButton');
    let filterCount = 0;

    addButton.addEventListener('click', function() {
        filterCount++;
        const filterDiv = document.createElement('div');
        filterDiv.className = 'd-flex gap-3 align-items-center';
        filterDiv.innerHTML = `
            <select name="filterField${filterCount}" class="form-control">
                <option value="ID">ID</option>
                <option value="Product">Product</option>
                <option value="BuyerEmail">Buyer Email</option>
                <option value="PurchaseDate">Purchase Date</option>
                <option value="Country">Country</option>
                <option value="Price">Price</option>
                <option value="Refunded">Refunded</option>
                <option value="Currency">Currency</option>
                <option value="Quantity">Quantity</option>
            </select>
            <input type="text" name="filterValue${filterCount}" class="form-control" placeholder="Filter value">
            <button type="button" class="btn btn-danger removeButton">Remove</button>
        `;
        inputContainer.appendChild(filterDiv);

        const removeButton = filterDiv.querySelector('.removeButton');
        removeButton.addEventListener('click', function() {
            inputContainer.removeChild(filterDiv);
            if (inputContainer.children.length === 0) {
                submitButton.style.display = 'none';
            }
        });

        submitButton.style.display = 'block';
    });
});
