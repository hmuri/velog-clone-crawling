function changeTheme() {
  const body = document.querySelector("body");
  body.style.backgroundColor =
    body.style.backgroundColor === "black" ? "#efefef" : "black";
  body.style.color = body.style.color === "white" ? "black" : "white";
  const nav = document.querySelector("nav ul");
  nav.style.color = nav.style.color === "#333" ? "white" : "#333";
}

function changeColor(selectedItem) {
  // 모든 항목에서 "selected" 클래스 제거
  const items = document.querySelectorAll(".select-order");
  items.forEach((item) => item.classList.remove("selected"));

  // 선택된 항목에 "selected" 클래스 추가
  selectedItem.classList.add("selected");
}

function fetchData(endpoint) {
  fetch(endpoint)
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        const postData = data.data;
        displayPosts(postData);
      }
    });
}

function displayPosts(postData) {
  const container = document.querySelector(".posting-container");
  container.innerHTML = ""; // 기존 포스트 데이터를 지워줍니다.

  postData.forEach((post) => {
    const cardHTML = `
            <div class="posting-card">
                <a href="https://velog.io${post["post_url"]}" class="post-url">
                    <img src="${post["thumbnail_url"]}" alt="썸네일" class="thumbnail-url" />
                </a>
                <h4 class="title">${post["title"]}</h4>
                <div class="description-wrapper">
                    <p class="description">${post["description"]}</p>
                </div>
                <div class="sub-info">
                    <span class="date">${post["date"]}</span>
                    <span>|</span>
                    <span class="comment-count">댓글: ${post["comment_count"]}개</span>
                </div>
                <a href="#" class="userinfo">
                    <img src="${post["author_profile_url"]}" alt="작성자 프로필" class="author-profile-url" />
                    <b class="author-name">${post["author_name"]}</b>
                </a>
                <div class="likes">${post["likes"]} 좋아요</div>
            </div>
        `;

    container.insertAdjacentHTML("beforeend", cardHTML);
  });
}

// 페이지 로드 시 트렌딩 데이터 기본값
window.onload = function () {
  fetchData("/run-script");
};
