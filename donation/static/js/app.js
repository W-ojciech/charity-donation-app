document.addEventListener("DOMContentLoaded", function() {
  /**
   * HomePage - Help section
   */
  class Help {
    constructor($el) {
      this.$el = $el;
      this.$buttonsContainer = $el.querySelector(".help--buttons");
      this.$slidesContainers = $el.querySelectorAll(".help--slides");
      this.currentSlide = this.$buttonsContainer.querySelector(".active").parentElement.dataset.id;
      this.init();
    }

    init() {
      this.events();
    }

    events() {
      /**
       * Slide buttons
       */
      this.$buttonsContainer.addEventListener("click", e => {
        if (e.target.classList.contains("btn")) {
          this.changeSlide(e);
        }
      });

      /**
       * Pagination buttons
       */
      this.$el.addEventListener("click", e => {
        if (e.target.classList.contains("btn") && e.target.parentElement.parentElement.classList.contains("help--slides-pagination")) {
          this.changePage(e);
        }
      });
    }

    changeSlide(e) {
      e.preventDefault();
      const $btn = e.target;

      // Buttons Active class change
      [...this.$buttonsContainer.children].forEach(btn => btn.firstElementChild.classList.remove("active"));
      $btn.classList.add("active");

      // Current slide
      this.currentSlide = $btn.parentElement.dataset.id;

      // Slides active class change
      this.$slidesContainers.forEach(el => {
        el.classList.remove("active");

        if (el.dataset.id === this.currentSlide) {
          el.classList.add("active");
        }
      });
    }

    /**
     * TODO: callback to page change event
     */
    changePage(e) {
      e.preventDefault();
      const page = e.target.dataset.page;

      console.log(page);
    }
  }

  const helpSection = document.querySelector(".help");
  if (helpSection !== null) {
    new Help(helpSection);
  }

  /**
   * Form Select
   */
  class FormSelect {
    constructor($el) {
      this.$el = $el;
      this.options = [...$el.children];
      this.init();
    }

    init() {
      this.createElements();
      this.addEvents();
      this.$el.parentElement.removeChild(this.$el);
    }

    createElements() {
      // Input for value
      this.valueInput = document.createElement("input");
      this.valueInput.type = "text";
      this.valueInput.name = this.$el.name;

      // Dropdown container
      this.dropdown = document.createElement("div");
      this.dropdown.classList.add("dropdown");

      // List container
      this.ul = document.createElement("ul");

      // All list options
      this.options.forEach((el, i) => {
        const li = document.createElement("li");
        li.dataset.value = el.value;
        li.innerText = el.innerText;

        if (i === 0) {
          // First clickable option
          this.current = document.createElement("div");
          this.current.innerText = el.innerText;
          this.dropdown.appendChild(this.current);
          this.valueInput.value = el.value;
          li.classList.add("selected");
        }

        this.ul.appendChild(li);
      });

      this.dropdown.appendChild(this.ul);
      this.dropdown.appendChild(this.valueInput);
      this.$el.parentElement.appendChild(this.dropdown);
    }

    addEvents() {
      this.dropdown.addEventListener("click", e => {
        const target = e.target;
        this.dropdown.classList.toggle("selecting");

        // Save new value only when clicked on li
        if (target.tagName === "LI") {
          this.valueInput.value = target.dataset.value;
          this.current.innerText = target.innerText;
        }
      });
    }
  }

  document.querySelectorAll(".form-group--dropdown select").forEach(el => {
    new FormSelect(el);
  });

  /**
   * Hide elements when clicked on document
   */
  document.addEventListener("click", function(e) {
    const target = e.target;
    const tagName = target.tagName;

    if (target.classList.contains("dropdown")) return false;

    if (tagName === "LI" && target.parentElement.parentElement.classList.contains("dropdown")) {
      return false;
    }

    if (tagName === "DIV" && target.parentElement.classList.contains("dropdown")) {
      return false;
    }

    document.querySelectorAll(".form-group--dropdown .dropdown").forEach(el => {
      el.classList.remove("selecting");
    });
  });

  /**
   * Switching between form steps
   */
  class FormSteps {
    constructor(form) {
      this.$form = form;
      this.$next = form.querySelectorAll(".next-step");
      this.$prev = form.querySelectorAll(".prev-step");
      this.$step = form.querySelector(".form--steps-counter span");
      this.currentStep = 1;

      this.$stepInstructions = form.querySelectorAll(".form--steps-instructions p");
      const $stepForms = form.querySelectorAll("form > div");
      this.slides = [...this.$stepInstructions, ...$stepForms];

      this.init();
    }

    /**
     * Init all methods
     */
    init() {
      this.events();
      this.updateForm();
    }

    /**
     * All events that are happening in form
     */
    events() {
      let div_steps_instructions = form.querySelector(".form--steps-instructions");
      let div_steps_counter = form.querySelector(".form--steps-counter");
      // Next step
      this.$next.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep++;
          this.updateForm();
          if (this.currentStep === 5) {
            div_steps_instructions.style.display = 'none';
            div_steps_counter.style.display = 'none';
          }
        });
      });

      // Previous step
      this.$prev.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep--;
          this.updateForm();
          if (this.currentStep < 5) {
            div_steps_instructions.style.display = 'block';
            div_steps_counter.style.display = 'block';
          }
        });
      });

      // Form submit
      this.$form.querySelector("form").addEventListener("submit", e => this.submit(e));
    }

    /**
     * Update form front-end
     * Show next or previous section etc.
     */
    updateForm() {
      this.$step.innerText = this.currentStep;

      // TODO: Validation

      this.slides.forEach(slide => {
        slide.classList.remove("active");

        if (slide.dataset.step == this.currentStep) {
          slide.classList.add("active");
        }
      });

      // this.$stepInstructions[0].parentElement.parentElement.hidden = this.currentStep >= 6;
      // this.$step.parentElement.hidden = this.currentStep >= 6;

      // if (this.currentStep >= 6) {
      //   this.$form.submit()
      // }

      // TODO: get data from inputs and show them in summary
    }

    /**
     * Submit form
     *
     * TODO: validation, send data to server
     */
    submit(e) {
      e.preventDefault();
      this.currentStep++;
      this.updateForm();
    }
  }

  const form = document.querySelector(".form--steps");
  if (form !== null) {
    new FormSteps(form);
  }




  /**
   * Wyświetlanie tylko tych instytucji, które mają zaznaczony checkbox w kroku 1
   */
  let institution_categories = document.querySelectorAll('.categories-hidden');
  let checkboxes_step1 = document.querySelectorAll('.input-step1');
  checkboxes_step1.forEach(checkbox => {
    checkbox.addEventListener('click', el => {
      let values_list = [];
      checkboxes_step1.forEach(checkbox => {
        if(checkbox.checked === true){
          values_list.push(checkbox.value)
        }
      });
      console.log('wyświetlam listę values_list:', values_list);

      institution_categories.forEach(category => {
        let allowed_categories = JSON.parse(category.getAttribute('data-allowed-categories'));
        console.log('allowed_categories', allowed_categories);
        category.parentElement.parentElement.style.display = 'none';
        values_list.forEach(el => {
          if (allowed_categories.includes(el) === true) {
            category.parentElement.parentElement.style.display = 'block'
          }
          else {
            category.parentElement.parentElement.style.display = 'none'
          }
        })
      })
    })
  });



  /**
   * Przekazywanie do kroku 5 ilości worków oraz kategorii zaznaczonych w kroku 1
   */
  let btn_next_step1 = document.querySelector('#btn-next-step1');
  let step5_bag = document.querySelector('.step5-bag');
  checkboxes_step1.forEach(checkbox => {
    checkbox.addEventListener('click', el => {
      let checked_inst_list =[];
      checkboxes_step1.forEach(checkbox => {
        if (checkbox.checked === true) {
          checked_inst_list.push(checkbox.nextElementSibling.nextElementSibling.innerHTML)
        }
      });

      btn_next_step1.addEventListener('click', el => {
        let btn_next_step2 = document.querySelector('#btn-next-step2');
        btn_next_step2.addEventListener('click', el => {
          let bag = document.querySelector('.bag');
          let bag_quantity = parseInt(bag.value);
          if (1 < bag_quantity < 5)
            step5_bag.innerText = `Oddajesz: ${checked_inst_list} - ${bag_quantity} worki`;
          if (bag_quantity > 4)
            step5_bag.innerText = `Oddajesz: ${checked_inst_list} - ${bag_quantity} worków`;
          else {
            step5_bag.innerText = "Oddajesz: " + checked_inst_list + " - " + bag_quantity + " worek";
          }
        });
      });
      console.log('checked_inst_list', checked_inst_list);
    })
  });



  /**
   * Przekazywanie do kroku 5 wybranej instytucji w kroku 3
   */
  let radio_step3 = document.querySelectorAll('[type="radio"]');
  let step5_inst = document.querySelector('.step5-inst');

  radio_step3.forEach(el => {
    el.addEventListener('click', el => {
      radio_step3.forEach(el => {
        if (el.checked === true){
          let name_of_inst = el.nextElementSibling.nextElementSibling.firstElementChild.innerHTML
          step5_inst.innerHTML = "Dla fundacji " + name_of_inst;

          console.log("Nazwa wybranej instytucji:", name_of_inst);
          let id_wybranej_instytucji = el.value;
          console.log('id_wybranej_instytucji:', id_wybranej_instytucji);
        }
      });
     })
  });



  /**
   * Przekazywanie do kroku 5 danych podanych w kroku 4
   */
  let address_ul = document.querySelector('#address');
  let time_ul = document.querySelector('#time');
  let button_next_step4 = document.querySelector('#button-next-step4');

  button_next_step4.addEventListener('click', el => {
    let street = document.querySelector('[name="address"]').value;
    let city = document.querySelector('[name="city"]').value;
    let postcode = document.querySelector('[name="postcode"]').value;
    let phone = document.querySelector('[name="phone"]').value;
    let data2 = document.querySelector('[name="data"]').value;
    let time2 = document.querySelector('[name="time"]').value;
    let more_info = document.querySelector('[name="more_info"]').value;

    address_ul.firstElementChild.innerHTML = street;
    address_ul.firstElementChild.nextElementSibling.innerHTML = city;
    address_ul.firstElementChild.nextElementSibling.nextElementSibling.innerHTML = postcode;
    address_ul.lastElementChild.innerHTML = phone;

    time_ul.firstElementChild.innerHTML = data2;
    time_ul.firstElementChild.nextElementSibling.innerHTML = time2;
    time_ul.lastElementChild.innerHTML = more_info;
  });



  // let confirm_form = document.querySelector('[type="submit"]');
  // confirm_form.addEventListener('click', el => {
  //   console.log('potwierdzenie:', confirm_form);
  // });


  // let donation_id = document.querySelector('#donation-id').value;
  // let donantion_button = document.querySelector('#donation-id');
  // donantion_button.addEventListener('click', el => {
  //   el.preventDefault();
  //   console.log('numer dotacji: ', donation_id)
  // });
  //
  // console.log('numer dotacji: ', donation_id)


  let donations = document.querySelectorAll('.taken-or-not');
  donations.addEventListener('onload', el => {
    el.initEvent();
    donations.forEach(el => {
    if (el.firstElementChild.innerHTML === 'odebrane') {
      el.parentElement.style.backgroundColor = 'red';
    }
  })
  });


});

