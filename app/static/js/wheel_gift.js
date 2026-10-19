        const canvas = document.getElementById("wheelCanvas");
        const ctx = canvas.getContext("2d");
        const pointer = document.getElementById("pointer");
        const wheelTrigger = document.getElementById("wheelTrigger");
        const modal = document.getElementById("resultModal");
        const winnerText = document.getElementById("winnerText");
        const winSound = new Audio('/static/audio/chuc_mung.mp3');

        let segments = [];
        let numSegments = 0;
        let anglePerSegment = 0;
        let currentRotation = 0;
        let isSpinning = false;
        let lastWinnerIndex = -1;

        function triggerFireworks() {
    const canvas = document.getElementById('myConfettiCanvas');
    const myConfetti = confetti.create(canvas, {
                resize: true,
                useWorker: true
            });

            myConfetti({
                particleCount: 150,
                spread: 80,
                origin: { y: 0.6 }
            });
        }

        async function loadData() {
            try {
                const response = await fetch('/get_gifts');
                const data = await response.json();
                segments = data.users;
                updateWheelConfig();
            } catch (error) {
                console.error("Lỗi khi tải dữ liệu từ server:", error);
            }
        }

        async function resetData() {
            if (isSpinning) return;
            try {
                const response = await fetch('/reset_gifts', { method: 'POST' });
                const data = await response.json();
                segments = data.users;
                currentRotation = 0;
                updateWheelConfig();
            } catch (error) {
                console.error("Lỗi khi reset:", error);
            }
        }

        function updateWheelConfig() {
            numSegments = segments.length;
            if (numSegments > 0) {
                anglePerSegment = (2 * Math.PI) / numSegments;
            } else {
                pointer.style.backgroundColor = "transparent";
            }
            drawWheel(currentRotation);
            updatePointerColor();
        }

        function drawWheel(rotation) {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            if (numSegments === 0) {
                ctx.fillStyle = "white";
                ctx.font = "bold 40px sans-serif";
                ctx.textAlign = "center";
                ctx.fillText("Chưa có dữ liệu hoặc đã xóa hết!", canvas.width/2, canvas.height/2);
                return;
            }

            const centerX = canvas.width / 2;
            const centerY = canvas.height / 2;
            const radius = centerX;

            for (let i = 0; i < numSegments; i++) {
                const startAngle = rotation + i * anglePerSegment;
                const endAngle = startAngle + anglePerSegment;

                ctx.beginPath();
                ctx.moveTo(centerX, centerY);
                ctx.arc(centerX, centerY, radius, startAngle, endAngle);
                ctx.fillStyle = segments[i].color;
                ctx.fill();
                ctx.lineWidth = 2;
                ctx.strokeStyle = "rgba(255,255,255,0.4)";
                ctx.stroke();

                ctx.save();
                ctx.translate(centerX, centerY);
                ctx.rotate(startAngle + anglePerSegment / 2);
                ctx.textAlign = "right";
                ctx.textBaseline = "middle";
                ctx.fillStyle = "#333";
                ctx.font = "bold 32px sans-serif";
                ctx.fillText(segments[i].text, radius - 50, 0);
                ctx.restore();
            }

            ctx.beginPath();
            ctx.arc(centerX, centerY, radius * 0.12, 0, 2 * Math.PI);
            ctx.fillStyle = "white";
            ctx.shadowColor = 'rgba(0,0,0,0.4)';
            ctx.shadowBlur = 15;
            ctx.fill();
            ctx.shadowColor = 'transparent';
        }

        function updatePointerColor() {
            if (numSegments === 0) return;
            let normalizedRotation = currentRotation % (2 * Math.PI);
            let pointingAngle = (2 * Math.PI - normalizedRotation) % (2 * Math.PI);
            let currentIndex = Math.floor(pointingAngle / anglePerSegment);
            pointer.style.backgroundColor = segments[currentIndex].color;
        }

        function animateSpin(targetRotation, duration, targetIndex) {
            const startTime = performance.now();
            const startRotation = currentRotation;
            const rotationChange = targetRotation - startRotation;

            function animate(currentTime) {
                const elapsed = currentTime - startTime;
                const progress = Math.min(elapsed / duration, 1);
                const easeOut = 1 - Math.pow(1 - progress, 3.5);

                currentRotation = startRotation + rotationChange * easeOut;

                drawWheel(currentRotation);
                updatePointerColor();

                if (progress < 1) {
                    requestAnimationFrame(animate);
                } else {
                    isSpinning = false;
                    showResult(targetIndex);
                }
            }
            requestAnimationFrame(animate);
        }

        function showResult(index) {
            lastWinnerIndex = index;
            winnerText.innerText = segments[index].text;
            winSound.currentTime = 0;
            winSound.play().catch(error => {
                console.log("Trình duyệt chặn tự động phát âm thanh:", error);
            });
            triggerFireworks();
            modal.classList.add("show");
        }

        function handleKeep() {
            modal.classList.remove("show");
        }

        async function handleDelete() {
            modal.classList.remove("show");
            const deletedUser = segments[lastWinnerIndex];

            try {
                await fetch('/delete_gift', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ id: deletedUser.id })
                });

                segments.splice(lastWinnerIndex, 1);
                updateWheelConfig();

            } catch (error) {
                console.error("Lỗi khi xóa trên server:", error);
                alert("Có lỗi xảy ra khi đồng bộ xóa với máy chủ!");
            }
        }

        wheelTrigger.addEventListener("click", async () => {
            if (isSpinning || numSegments === 0) return;
            isSpinning = true;

            try {
                const response = await fetch(`/random-gifts?total=${numSegments}`);
                const data = await response.json();
                const targetId = data.winnerId;

                const targetIndex = segments.findIndex(user => user.id === targetId);

                if (targetIndex === -1) {
                    console.error("Lỗi: Backend trả về ID không tồn tại trên vòng quay!");
                    isSpinning = false;
                    return;
                }

                const targetAngle = targetIndex * anglePerSegment + (anglePerSegment / 2);
                const randomOffset = (Math.random() - 0.5) * (anglePerSegment * 0.7);

                let baseTargetRotation = 2 * Math.PI - (targetAngle + randomOffset);
                let currentMod = currentRotation % (2 * Math.PI);
                let diff = baseTargetRotation - currentMod;

                if (diff < 0) diff += 2 * Math.PI;

                const totalRotation = currentRotation + (7 * 2 * Math.PI) + diff;
                animateSpin(totalRotation, 4500, targetIndex);

            } catch (error) {
                console.error("Lỗi khi kết nối server quay số:", error);
                isSpinning = false;
            }
        });

        loadData();