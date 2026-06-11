(function () {
  'use strict';

  var SECS = 30;
  var CIRC = 2 * Math.PI * 18;

  var questions  = JSON.parse(document.getElementById('q-data').textContent);
  var categoryId = document.getElementById('cat-id').textContent.trim();
  var total      = questions.length;

  var current   = 0;
  var answers   = {};
  var timeLeft  = SECS;
  var ticker    = null;
  var submitted = false;

  var elQNum     = document.getElementById('q-num');
  var elQText    = document.getElementById('q-text');
  var elOptions  = document.getElementById('options');
  var elProgFill = document.getElementById('prog-fill');
  var elProgLbl  = document.getElementById('prog-lbl');
  var elTimerBox = document.getElementById('timer-box');
  var elTimerNum = document.getElementById('timer-num');
  var elArc      = document.getElementById('timer-arc');
  var elBtnPrev  = document.getElementById('btn-prev');
  var elBtnNext  = document.getElementById('btn-next');
  var elBtnSub   = document.getElementById('btn-submit');
  var elAnsCount = document.getElementById('ans-count');
  var elQGrid    = document.getElementById('q-grid');
  var elGridPct  = document.getElementById('grid-pct');
  var elModal    = document.getElementById('modal');
  var elModalMsg = document.getElementById('modal-msg');

  var LABELS = ['A', 'B', 'C', 'D'];

  function escHtml(str) {
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function renderQuestion() {
    var q = questions[current];

    elQNum.textContent  = 'Question ' + (current + 1) + ' of ' + total;
    elQText.textContent = q.question;

    elOptions.innerHTML = '';
    q.options.forEach(function (opt, i) {
      var selected = (answers[current] === i);
      var btn = document.createElement('button');
      btn.className = 'option-btn' + (selected ? ' option-btn--selected' : '');
      btn.innerHTML =
        '<span class="opt-key">' + LABELS[i] + '</span>' +
        '<span class="opt-text">' + escHtml(opt) + '</span>';
      btn.addEventListener('click', function () { selectAnswer(i); });
      elOptions.appendChild(btn);
    });

    var pct = Math.round(((current + 1) / total) * 100);
    elProgFill.style.width = pct + '%';
    elProgLbl.textContent  = 'Question ' + (current + 1) + ' of ' + total;

    elBtnPrev.disabled          = (current === 0);
    elBtnNext.style.display     = current < total - 1 ? 'inline-flex' : 'none';
    elBtnSub.style.display      = current === total - 1 ? 'inline-flex' : 'none';

    refreshGrid();
    refreshAnsCount();
    resetTimer();
  }

  function selectAnswer(idx) {
    answers[current] = idx;
    elOptions.querySelectorAll('.option-btn').forEach(function (btn, i) {
      btn.className = 'option-btn' + (i === idx ? ' option-btn--selected' : '');
    });
    refreshGrid();
    refreshAnsCount();
  }

  function resetTimer() {
    clearInterval(ticker);
    timeLeft = SECS;
    paintTimer();
    ticker = setInterval(function () {
      timeLeft -= 1;
      paintTimer();
      if (timeLeft <= 0) {
        clearInterval(ticker);
        if (answers[current] === undefined) answers[current] = -1;
        if (current < total - 1) {
          current += 1;
          renderQuestion();
        } else {
          doSubmit();
        }
      }
    }, 1000);
  }

  function paintTimer() {
    var s = timeLeft;
    elTimerNum.textContent = (s < 10 ? '0' : '') + s;

    var offset = CIRC - (s / SECS) * CIRC;
    if (elArc) elArc.style.strokeDashoffset = offset;

    var col, cls;
    if (s <= 5) {
      col = 'var(--c-danger)';  cls = 'timer timer--crit';
    } else if (s <= 10) {
      col = 'var(--c-warning)'; cls = 'timer timer--warn';
    } else {
      col = 'var(--c-primary)'; cls = 'timer';
    }

    elTimerNum.style.color = col;
    if (elArc) elArc.style.stroke = col;
    elTimerBox.className = cls;
  }

  function buildGrid() {
    elQGrid.innerHTML = '';
    for (var i = 0; i < total; i++) {
      (function (idx) {
        var btn = document.createElement('button');
        btn.className = 'q-grid__btn';
        btn.textContent = idx + 1;
        btn.addEventListener('click', function () {
          current = idx;
          renderQuestion();
        });
        elQGrid.appendChild(btn);
      })(i);
    }
  }

  function refreshGrid() {
    elQGrid.querySelectorAll('.q-grid__btn').forEach(function (btn, i) {
      if (i === current) {
        btn.className = 'q-grid__btn q-grid__btn--current';
      } else if (answers[i] !== undefined) {
        btn.className = 'q-grid__btn q-grid__btn--done';
      } else {
        btn.className = 'q-grid__btn';
      }
    });
    var done = Object.keys(answers).length;
    elGridPct.textContent = Math.round((done / total) * 100) + '%';
  }

  function refreshAnsCount() {
    var done = Object.keys(answers).length;
    elAnsCount.textContent = done + ' / ' + total + ' answered';
  }

  function openModal() {
    var done = Object.values(answers).filter(function (v) {
      return v !== undefined && v !== -1;
    }).length;
    var skipped = total - done;
    var msg = done + ' of ' + total + ' questions answered.';
    if (skipped > 0) {
      msg += ' ' + skipped + ' unanswered question' + (skipped !== 1 ? 's' : '') + ' will be marked as skipped.';
    }
    elModalMsg.textContent = msg;
    elModal.style.display  = 'flex';
  }

  function closeModal() {
    elModal.style.display = 'none';
  }

  async function doSubmit() {
    if (submitted) return;
    submitted = true;
    clearInterval(ticker);
    closeModal();

    var resp = await fetch('/submit', {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body:    JSON.stringify({ category: categoryId, answers: answers }),
    });
    var data = await resp.json();
    if (data.ok) window.location.href = '/result';
  }

  elBtnPrev.addEventListener('click', function () {
    if (current > 0) { current -= 1; renderQuestion(); }
  });

  elBtnNext.addEventListener('click', function () {
    if (current < total - 1) { current += 1; renderQuestion(); }
  });

  elBtnSub.addEventListener('click', openModal);
  document.getElementById('modal-confirm').addEventListener('click', doSubmit);
  document.getElementById('modal-cancel').addEventListener('click', closeModal);

  var earlyBtn = document.getElementById('btn-early-sub');
  if (earlyBtn) earlyBtn.addEventListener('click', openModal);

  buildGrid();
  renderQuestion();

})();
