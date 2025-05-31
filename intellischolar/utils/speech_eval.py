import whisper
import tempfile
from difflib import SequenceMatcher
from jiwer import wer, Compose, ToLowerCase, RemovePunctuation, Strip, RemoveWhiteSpace, RemoveMultipleSpaces

# WER 正規化パイプライン
transform = Compose([
    ToLowerCase(),
    RemovePunctuation(),
    Strip(),
    RemoveWhiteSpace(replace_by_space=True),
    RemoveMultipleSpaces()
])

def evaluate_pronunciation(audio_file):
    # Whisper モデルを関数内でロード
    model = whisper.load_model("base")

    # 一時ファイルに保存
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_file.read())
        tmp_path = tmp.name

    # Whisper で文字起こし
    result = model.transcribe(tmp_path, language="en")
    predicted_text = result["text"].strip()

    # 正解（今後はユーザー入力連携可能に）
    reference_text = (
        "Hello, my name is Shusei Abe, a computer science student specializing in artificial intelligence and data science "
        "at Estelle-Haji Karoye Kotori University. Today, I'd like to introduce Spacio, a project designed just to solve a problem, "
        "but received away sizzling space. Across Hungary and much of the world, she is facing silent classes, in-eff-shan parking, "
        "on-cops-cops-space usage. Kakkuru is for parking, delivery runs block traffic, and sidewalks become dangerous. "
        "Despite technological progress, urban space remains unmanaged, chaotic, and wasteful. Spacio is a smart urban space optimization platform..."
    )

    # 正規化
    ref_clean = transform(reference_text)
    hyp_clean = transform(predicted_text)

    # エラーハンドリング
    if not ref_clean.strip() or not hyp_clean.strip():
        return 0.0, predicted_text + "\n⚠️ Warning: One of the texts is empty after normalization."

    try:
        wer_score = 1 - wer(ref_clean, hyp_clean)
    except Exception as e:
        return 0.0, predicted_text + f"\n⚠️ WER calculation failed: {str(e)}"

    # 類似度スコア（SequenceMatcher）
    sim_score = SequenceMatcher(None, reference_text.lower(), predicted_text.lower()).ratio()

    # 複合スコア（重み付き平均）
    score = round((wer_score * 0.6 + sim_score * 0.4) * 10, 1)

    # デバッグ情報を付加（Streamlit用に表示しやすい形式）
    feedback = (
        f"🎯 Predicted Text:\n{predicted_text}\n\n"
        f"📘 Reference Text:\n{reference_text}\n\n"
        f"📊 WER Score: {wer_score:.2f}, Similarity: {sim_score:.2f}, Final Score: {score}"
    )

    return score, feedback
