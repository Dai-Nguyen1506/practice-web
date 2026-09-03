function renderUsers(users) {
  let tableBody = document.querySelector("#user-table tbody");
  tableBody.innerHTML = "";
  users.forEach((user) => {
    const row = document.createElement("tr");
    row.innerHTML = `
            <td>${user.id}</td>
            <td>${user.name}</td>
            <td>${user.phone}</td>
            <td>${user.email.toLowerCase()}</td>
            <td>${user.website}</td>
            <td>${user.address.street + " - " + user.address.city}</td>
        `;
    tableBody.appendChild(row);
  });
}

// function fetchUsers() {
//   fetch(" https://jsonplaceholder.typicode.com/users")
//     .then((response) => {
//       return response.json();
//     })
//     .then((users) => renderUsers(users));
// }

async function fetchUsers() {
  let users;
  try {
    const res = await fetch("https://jsonplaceholder.typicode.com/users");
    users = await res.json();
  } catch (error) {
    console.error("Error fetching users:", error);
  } finally {
    renderUsers(users);
  }
}

async function reset() {
  let tableBody = document.querySelector("#user-table tbody");
  tableBody.innerHTML = "";
}
