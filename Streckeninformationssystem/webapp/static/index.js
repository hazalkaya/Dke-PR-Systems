function deleteTrainstation(trainstationId) {
  fetch("/delete-trainstation", {
    method: "POST",
    body: JSON.stringify({ trainstationId: trainstationId }),
  }).then((_res) => {
    window.location.href = "/all_trainstations";
  });
}
function deleteUser(userId) {
  fetch("/delete-user", {
    method: "POST",
    body: JSON.stringify({ userId: userId }),
  }).then((_res) => {
    window.location.href = "/all_users";
  });
}