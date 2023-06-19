const registrationForm = document.getElementById('registration-form');
const registrationStatus = document.getElementById('registration-status');
const groupSelect = document.getElementById('group');

// Fetch group options from the backend
axios.get('http://127.0.0.1:8000/api/groups/')  // Replace with your group names API endpoint URL
  .then(response => {
    response.data.forEach(group => {
      const option = document.createElement('option');
      option.value = group.name;
      option.text = group.name;
      groupSelect.appendChild(option);
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });

registrationForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;
  const email = document.getElementById('email').value;
  const firstName = document.getElementById('first-name').value;
  const lastName = document.getElementById('last-name').value;
  const group = groupSelect.value; // Use the selected value from the groupSelect element

  const userData = {
    username: username,
    password: password,
    email: email,
    first_name: firstName,
    last_name: lastName,
    group: group
  };

  console.log(userData)

  axios.post('http://127.0.0.1:8000/api/user/register/', userData)  // Replace with your user registration API endpoint URL
    .then(response => {
      const registrationMessage = `User ${response.data.username} registered successfully.`;
      registrationStatus.textContent = registrationMessage;
    })
    .catch(error => {
      console.error('Error:', error);
      registrationStatus.textContent = 'Registration failed.';
    });
});
