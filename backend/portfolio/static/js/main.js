class Navigation {
            static init() {
                this.setupMobileMenu();
                this.setupSmoothScrolling();
                this.setupActiveNavLinks();
                this.setupTimelineReveal();
                this.setupRevealAnimations();
            }

            static setupMobileMenu() {
                const hamburger = document.querySelector('.hamburger');
                const navMenu = document.querySelector('.nav-menu');

                if (hamburger && navMenu) {
                    hamburger.addEventListener('click', () => {
                        hamburger.classList.toggle('open');
                        navMenu.classList.toggle('active');
                    });

                    document.querySelectorAll('.nav-link').forEach(link => {
                        link.addEventListener('click', () => {
                            if(navMenu.classList.contains('active')) {
                                navMenu.classList.remove('active');
                                hamburger.classList.remove('open');
                            }
                        });
                    });
                }
            }

            static setupSmoothScrolling() {
                document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                    anchor.addEventListener('click', function (e) {
                        e.preventDefault();
                        const target = document.querySelector(this.getAttribute('href'));
                        if (target) {
                            const offset = 70; // account for fixed navbar height
                            const bodyRect = document.body.getBoundingClientRect().top;
                            const targetRect = target.getBoundingClientRect().top;
                            const targetPosition = targetRect - bodyRect - offset;

                            window.scrollTo({
                                top: targetPosition,
                                behavior: 'smooth'
                            });
                        }
                    });
                });
            }

            static setupActiveNavLinks() {
                const sections = document.querySelectorAll('section');
                const navLinks = document.querySelectorAll('.nav-link');

                window.addEventListener('scroll', () => {
                    let current = '';
                    sections.forEach(section => {
                        const sectionTop = section.offsetTop;
                        if (pageYOffset >= sectionTop - 100) {
                            current = section.getAttribute('id');
                        }
                    });

                    navLinks.forEach(link => {
                        link.classList.remove('active');
                        if (link.getAttribute('href') === `#${current}`) {
                            link.classList.add('active');
                        }
                    });
                });
            }

            static setupTimelineReveal() {
                const timelineItems = document.querySelectorAll(".timeline-content");

                const observer = new IntersectionObserver((entries) => {
                    entries.forEach((entry) => {
                        if (entry.isIntersecting) {
                            entry.target.classList.add("reveal");
                        }
                    });
                }, { threshold: 0.15 });

                timelineItems.forEach(item => observer.observe(item));
            }

            static setupRevealAnimations() {
                const revealElements = document.querySelectorAll(".reveal");

                const revealOnScroll = () => {
                    revealElements.forEach((el) => {
                        const elementTop = el.getBoundingClientRect().top;
                        const windowHeight = window.innerHeight;

                        if (elementTop < windowHeight - 100) {
                            el.classList.add("active");
                        }
                    });
                };

                window.addEventListener("scroll", revealOnScroll);
                window.addEventListener("DOMContentLoaded", revealOnScroll);
            }
        }

        document.addEventListener('DOMContentLoaded', function() {
            Navigation.init();

            window.addEventListener('scroll', () => {
                const navbar = document.querySelector('.navbar');
                if (window.scrollY > 100) {
                    navbar.style.background = 'rgba(255, 255, 255, 0.98)';
                    navbar.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1)';
                } else {
                    navbar.style.background = 'rgba(255, 255, 255, 0.95)';
                    navbar.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1)';
                }
            });
        });