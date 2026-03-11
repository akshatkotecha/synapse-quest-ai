def compute_leaderboard(users_behavior, users_code_score):

    leaderboard = []

    for user, behavior in users_behavior.items():

        norm_activity = min(behavior["activity"] / 5, 1)
        norm_speed = min(behavior["speed"] / 1, 1)
        norm_consistency = behavior["consistency"]

        behavior_score = (
            0.4 * norm_activity +
            0.3 * norm_consistency +
            0.3 * norm_speed
        )

        # Normalize code score (0-100 → 0-1)
        code_score = users_code_score.get(user, 0) / 100

        # Combine
        final_score = (
            0.6 * behavior_score +
            0.4 * code_score
        )

        leaderboard.append({
            "user": user,
            "score": round(final_score, 3)
        })

    leaderboard.sort(key=lambda x: x["score"], reverse=True)
    return leaderboard

