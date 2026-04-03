import streamlit as st

from utils import get_explanation


st.set_page_config(
    page_title="ELI5 Engineer",
    page_icon="⚙️",
    layout="centered",
)


def main() -> None:
    st.title("ELI5 Engineer")
    st.caption(
        "Understand engineering concepts through simple analogies, technical depth, "
        "and practical real-world examples."
    )

    st.markdown(
        "Enter any engineering topic, from foundational ideas like `load balancing` "
        "to advanced systems like `PID control` or `transformer architectures`."
    )

    with st.form("explain_form"):
        topic = st.text_input(
            "Engineering topic",
            placeholder="e.g. finite element analysis",
        )
        submitted = st.form_submit_button("Explain", use_container_width=True)

    if not submitted:
        return

    cleaned_topic = topic.strip()
    if not cleaned_topic:
        st.warning("Please enter an engineering topic before clicking Explain.")
        return

    with st.spinner("Generating your explanation..."):
        try:
            explanation = get_explanation(cleaned_topic)
        except ValueError as exc:
            st.warning(str(exc))
            return
        except RuntimeError as exc:
            st.error(str(exc))
            return
        except Exception:
            st.error(
                "Something unexpected happened while generating the explanation. "
                "Please try again."
            )
            return

    st.markdown("## Explanation")
    st.markdown(explanation)


if __name__ == "__main__":
    main()
