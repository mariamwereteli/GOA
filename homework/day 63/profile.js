function createProfile() {
    var firstName = document.getElementById('firstName').value;
    var lastName = document.getElementById('lastName').value;
    var age = document.getElementById('age').value;
    var dob = document.getElementById('dob').value;

    document.getElementById('profileFirstName').textContent = "First Name: " + firstName;
    document.getElementById('profileLastName').textContent = "Last Name: " + lastName;
    document.getElementById('profileAge').textContent = "Age: " + age;
    document.getElementById('profileDob').textContent = "Date of Birth: " + dob;
}

document.getElementById('createProfileButton').addEventListener('click', createProfile);
